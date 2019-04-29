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

1. Download discordrpblender.py from this repository.

2. Open discordrpblender.py and paste the client ID on **line 21** (replacing the template ID).

3. In the terminal, run `uname -i`:
	1. If the output is `x86` then download `Blender2.79-Linux32.zip`
	2. If the output is `x86_64` then download `Blender2.79-Linux64.zip`

5. Extract it wherever you want to keep it.

6. Run it with `blender -P PATH_TO_SCRIPT/discordrpblender.py`

##### Windows
Do exactly the same as above, but download `Blender2.79-Windows32.zip` or `Blender2.79-Windows64.zip` depending on if your PC is 32bit or 64bit. Here's how to check:

https://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/

##### Mac
???

### Blender 2.79 installed
Even simpler!

# Installation

1. Install **discoIPC** by running `pip install discoIPC`.

2. Download the Discord app and log in.

3. Enable game activity status on Discord.

Now to set up a Discord application to receive Blender rich presence.

4. Visit https://discordapp.com/developers/applications/

5. Create an application called Blender.

6. Click **Rich Presence** on the side bar and then scroll down.

7. Download the Blender logo from the "Images" folder in this repository

8. Go back to the Discord application.

9. Click **Add Image(s)** then upload the image you just downloaded.

10. Now download discordrpblender.py from this repository.

11. Open discordrpblender.py and paste the client ID on **line 21** (replacing the template ID).

And that's it! Now you may place the script wherever you like. Onto running it in Blender!

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

