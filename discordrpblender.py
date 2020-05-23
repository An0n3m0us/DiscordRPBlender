import bpy, subprocess
from bpy.app.handlers import persistent
import time, datetime, os, atexit
from discoIPC import ipc

from sys import platform

# Settings
showFilename = True;
showTimeElapsed = True;

base_activity = {
    'assets': {
        'large_image': 'blender',
        'large_text': 'Blender',
    },
    'timestamps': {},
}

pid = os.getpid()
filename = ''
objcount = 0
timeElapsed = int(time.time())
active = 0
rendering = 0
rendertime = 0

client = ipc.DiscordIPC('000000000000000000') # Replace your clientID with the 18 digit template
client.connect()
print('\nStarting Discord ICP ...\n')

@atexit.register
def disconnect():
    main()
    print('Disconnecting Discord ICP ...\n')
    client.disconnect()

@persistent
def main():
    client.update_activity(set_activity())

@persistent
def resetTime(scene):
    bpy.ops.wm.modal_timer_operator()
    global timeElapsed
    timeElapsed = int(time.time())

@persistent
def render_begin(scene):
    global rendering
    global rendertime
    global active
    rendering = 1
    active = 2
    rendertime = int(time.time())

@persistent
def render_cancel(scene):
    global rendering
    global rendertime
    global active
    rendering = 0
    rendertime = 0
    active = 1

@persistent
def render_complete(scene):
    global rendering
    global rendertime
    global active
    rendering = 0
    rendertime = 0
    #time_taken = int(time.time()) - int(rendertime)
    #time_end = int(time.time())
    active = 1

@persistent
def set_activity():
    global rendering
    global rendertime
    global objcount

    #Loop these variables
    objcount = len(bpy.data.objects)
    if platform == "linux" or platform == "linux2":
        if not subprocess.getstatusoutput('xdotool')[0] == 0:
            pidcheck = subprocess.getstatusoutput('xdotool getwindowfocus getwindowpid')[1]

            if not str(pidcheck) != str(pid):
                if rendering == 1:
                    active = 2
                else:
                    active = 0
            else:
                if rendering == 1:
                    active = 2
                else:
                    active = 1
    else:
        if rendering == 1:
            active = 2
        else:
            active = 0

    #Set activity for the player
    activity = base_activity
    if bpy.context.selected_objects and rendering == 0:
        if bpy.context.object.type == "ARMATURE":
            if bpy.context.active_pose_bone:
                activity['details'] = bpy.context.object.name + " - " + bpy.context.active_bone.name
            else:
                activity['details'] = bpy.context.object.name
        else:
            activity['details'] = bpy.context.object.name
    else:
        activity['details'] = filename or "(Untitled)"

    if active == 0:
        if not bpy.context.selected_objects:
            activity['state'] = '(' + str(objcount) + ' objects)'
        else:
            activity['state'] = bpy.context.object.type[:1] + bpy.context.object.type[1:].lower()
    elif active == 1:
        activity['details'] = filename or "(Untitled)"
        activity['state'] = 'Idle'
    elif active == 2:
        activity['state'] = 'Rendering for ' + '0' + str(datetime.timedelta(seconds=((int(time.time() - rendertime))))) # Hacky

    if showTimeElapsed == True:
        activity['timestamps']['start'] = timeElapsed

    return activity

timerfile = 0
class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    _timer = None

    @persistent
    def modal(self, context, event):
        if event.type == 'TIMER':
            global filename
            global timerfile
            if showFilename == True:
                filename = bpy.path.basename(bpy.context.blend_data.filepath)[:-6]
			
            if time.time() - timerfile > 0.05:
                timerfile = time.time()
                main()

        return {'PASS_THROUGH'}

    @persistent
    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    @persistent
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

def register():
    bpy.utils.register_class(ModalTimerOperator)
    bpy.app.handlers.load_post.append(resetTime)
    bpy.app.handlers.render_pre.append(render_begin)
    bpy.app.handlers.render_cancel.append(render_cancel)
    bpy.app.handlers.render_complete.append(render_complete)
    bpy.app.handlers.load_post.append(resetTime)


def unregister():
    bpy.app.handlers.load_post.remove(resetTime)
    bpy.app.handlers.render_complete.remove(render_complete)
    bpy.app.handlers.render_cancel.append(render_cancel)
    bpy.app.handlers.render_pre.remove(render_begin)
    bpy.utils.unregister_class(ModalTimerOperator)


if __name__ == "__main__":
    register()

bpy.ops.wm.modal_timer_operator()
