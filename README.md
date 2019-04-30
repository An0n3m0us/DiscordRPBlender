# DiscordRPBlender

![Logo](https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/images/DiscordRPBlender.png)

(Notice: I will not be working much on this project until at least July.)

Discord rich presence for Blender. Tested in Blender **2.79**

(Big thanks to eKross for testing DiscordRPBlender on Windows!)

DiscordRPBlender supports:
- Filename
- Amount of objects / Idle status / Render status (No idle status for Windows and ?Mac? yet)
- Render time
- Time spent on project (not all-time just session time)
- Changing files without turning server off

DiscordRPBlender needs:
- Instantly stop sending to Discord after Blender turns off (keeps sending for a few seconds)
- Remove stats after quitting (Discord keeps showing weird stats for a few seconds after)
- Blender addon
- Something in Blender to show the user that DiscordRPBlender is running
- Toolbar button to toggle on/off
- Idle status on Windows & Mac:
  - https://stackoverflow.com/a/36419702
- Installation package that allows input of client ID too

# Images

This is what DiscordRPBlender looks like on Discord.

![Img1](https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/images/ImgIdle.png)

![Img2](https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/images/ImgWorking.png)

![Img3](https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/images/ImgRendering.png)

# Installation without Python or Pip
### Blender 2.8 installed
That's fine! We can download 2.79 without removing Blender 2.8!

##### Linux
1. Launch a terminal.

2. Check whether Linux is 32bit or 64bit by running `uname -i`
	1. If the output is `x86`:
		1. Copy `source <(curl -s https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/blender-linux-x86)` into the terminal and hit the enter key.
	2. If the output is `x86_64`:
		1. Copy `source <(curl -s https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/blender-linux-x86_64)` into the terminal and hit the enter key.

Sit back and watch the script download Blender 2.79 and download DiscoIPC! Blender 2.79 will be downloaded to `/tmp/blender-2.79b-linux...`. You can move the Blender folder to anywhere you like!

Now to set up `discordrpblender.py` and run it! (See chapter "Setting up discordrpblender.py" below)

##### Windows
(Note: Need a better way than the current way of installation. Maybe a .bat script similar to the Linux script above)

1. Check if your system is 32bit or 64bit. How to check:

https://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/

If it is 32bit, download: [Blender2.79-Windows32.zip](http://www.mediafire.com/file/x2pqmu8mq03szxw/Blender2.79-Windows32.zip/file)

If it is 64bit, download: [Blender2.79-Windows64.zip](http://www.mediafire.com/file/5yku17tvdi1iyk2/Blender2.79-Windows64.zip/file)

2. Extract to any directory you prefer.

Now to set up `discordrpblender.py` and run it! (See chapter "Setting up discordrpblender.py" below)
##### Mac
TODO

### Blender 2.79 installed
TODO

# Installation with Python and Pip

1. Install **discoIPC** by running `pip3 install discoIPC`.

2. Download the Discord app and log in.

3. Enable game activity status on Discord.

Now to set up a Discord application to receive Blender rich presence.

4. Visit https://discordapp.com/developers/applications/

5. Create an application called Blender.

6. Click **Rich Presence** on the side bar and then scroll down.

7. Download the Blender logo from the "Images" folder in this repository

8. Go back to the Discord application.

9. Click **Add Image(s)** then upload the image you just downloaded.

# Setting up discordrpblender.py

Download discordrpblender.py from this repository.

Open discordrpblender.py and paste the client ID on **line 21** (replacing the template ID).

**And that's it! Now you may place the script wherever you like. Onto running it in Blender!**

# Running
##### Linux
Open a terminal.

If Blender is installed then run:
`blender -P PATH_TO_SCRIPT/discordrpblender.py`

Otherwise go to the directory where Blender is installed then run Blender:
1. `cd blender_installation_directory`
2. `blender -P PATH_TO_SCRIPT/discordrpblender.py`

##### Mac
Open the terminal application, go to the directory where Blender is installed, and run the executable within the app bundle, with commands like this:
1. `cd /Applications/Blender`
2. `./blender.app/Contents/MacOS/blender -P PATH_TO_SCRIPT/discordrpblender.py`

##### Windows
Open the Command Prompt, go to the directory where Blender is installed, and then run Blender:
1. `cd c:\blender_installation_directory`
2. `blender -P PATH_TO_SCRIPT/discordrpblender.py`

And that's it! You'll need to run this command every time you want Discord rich presence for Blender.

If you need more information visit the manual:

[Blender Manual](https://docs.blender.org/manual/en/latest/render/workflows/command_line.html)

# Credits

Credit to [k3rn31p4nic](https://github.com/k3rn31p4nic/) for the [discoIPC](https://github.com/k3rn31p4nic/discoIPC) module for Python.

# License
[CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)

