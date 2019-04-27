import bpy
from bpy.app.handlers import persistent
import time, datetime, os, atexit
from discoIPC import ipc

base_activity = {
    'assets': {
        'large_image': 'blender',
        'large_text': 'Blender',
    },
    'timestamps': {},
}

filename = ''
objcount = 0
timeElapsed = int(time.time())
active = 0
rendering = 0
rendertime = 0

client = ipc.DiscordIPC('123456789123456789') # Replace the template ID with your ID
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
    if os.system('xdotool getwindowfocus getwindowname | grep -q Blender') == 0:
        if rendering == 1:
            active = 2
        else:
            active = 0
    else:
        if rendering == 1:
            active = 2
        else:
            active = 1

    #Set activity for the player
    activity = base_activity
    if filename == '':
        activity['details'] = 'Untitled'
    else:
        activity['details'] = filename
    if active == 0:
        activity['state'] = '(' + str(objcount) + ' objects)'
    elif active == 1:
        activity['state'] = 'Idle'
    elif active == 2:
        activity['state'] = 'Rendering for ' + '0' + str(datetime.timedelta(seconds=((int(time.time() - rendertime))))) # Hacky
    activity['timestamps']['start'] = timeElapsed
    return activity

class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    _timer = None

    @persistent
    def modal(self, context, event):
        if event.type == 'TIMER':
            global filename
            global timeElapsed
            global objcount
            filename = bpy.path.basename(bpy.context.blend_data.filepath)[:-6]
            main()

        return {'PASS_THROUGH'}

    @persistent
    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, context.window)
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
