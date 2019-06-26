# DiscordRPBlender

![Logo](https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/images/DiscordRPBlender.png)

#### Table of contents
   * [Installation](#installation)
      * [Installation - Blender 2.8 already installed](#installation---blender-28-already-installed)
         * [Linux](#linux)
         * [Windows](#windows)
         * [Mac](#mac---incomplete)
      * [Installation - Blender 2.79 installed](#installation---blender-279-installed)
      * [Setting up](#setting-up)
   * [Running](#running)
      * [Linux](#linux)
      * [Windows](#windows-1)
      * [Mac](#mac)
   * [Credits](#credits)
   * [License](#license)

Discord Rich Presence for Blender. Tested in Blender **2.79**

[Images](https://github.com/An0n3m0us/DiscordRPBlender/wiki/Images)

DiscordRPBlender currently supports:
- Filename
- Amount of objects / Idle status / Render status (No idle status for Windows and Mac yet)
- Render time
- Time spent on project (not all-time just session time)
- Changing files without turning server off

[Changelog](https://github.com/An0n3m0us/DiscordRPBlender/wiki/Changelog)


## Installation

DiscordRPBlender currently works in Blender 2.79 only.

First, get the Discord App which is available for Linux, Windows, Mac and other devices.

1. Download the Discord App and log in.

2. Enable Game Activity status on Discord.

Next, [set up a Discord Application](https://github.com/An0n3m0us/DiscordRPBlender/wiki/Creating-a-Discord-Application)

### Installation - Blender 2.8 already installed
That's fine! We can download 2.79 without removing Blender 2.8!

##### Linux
Launch a terminal then copy `source <(curl -s https://raw.githubusercontent.com/An0n3m0us/DiscordRPBlender/master/blender-linux)` into the terminal and hit the enter key.

Sit back and watch the script download Blender 2.79 and download DiscoIPC! The script will ask you for your client ID from your Discord Application, so input/paste it into the terminal when it says so.

And that's it! Blender 2.79 will be in `/tmp/blender-2.79b-linux...`. You can now move the Blender installation to anywhere you like! Now we can run the script with Blender.

Now go to the [Running](#running) chapter.

&nbsp;

##### Windows
(Note: Need a better way than the current way of installation. Maybe a .bat script similar to the Linux script above)

1. Check if your system is 32bit or 64bit. How to check:

https://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/

If it is 32bit, download: [Blender2.79-Windows32.zip](http://www.mediafire.com/file/x2pqmu8mq03szxw/Blender2.79-Windows32.zip/file)

If it is 64bit, download: [Blender2.79-Windows64.zip](http://www.mediafire.com/file/5yku17tvdi1iyk2/Blender2.79-Windows64.zip/file)

2. Extract to any directory you prefer.

Now continue onto the [Setting Up](#setting-up) chapter.

&nbsp;

##### Mac - Incomplete
(Note: Need a better way than the current way of installation. Script file similar to the Linux script above)
Make sure you have Pip3 and Python 3.5 or a newer version installed.
1. Install **discoIPC** by running `pip3 install discoIPC`.

2. Download Blender 2.79.

Now continue onto the [Setting Up](#setting-up) chapter.

&nbsp;

### Installation - Blender 2.79 installed
TODO

### Setting up

Download discordrpblender.py from this repository.

Open discordrpblender.py and paste your Discord Applications client ID on **line 21** (replacing the template ID).

**And that's it! Now you may place the script wherever you like. Onto running it in Blender!**

## Running
##### Linux
Open a terminal.

If Blender is installed then run:
`blender -P PATH_TO_SCRIPT/discordrpblender.py`

Otherwise go to the directory where Blender is installed then run Blender:
1. `cd blender_installation_directory`
2. `blender -P PATH_TO_SCRIPT/discordrpblender.py`

If the file is in the Blender installation directory, you can run:
`blender -P discordrpblender.py`

##### Windows
Open the Command Prompt, go to the directory where Blender is installed, and then run Blender:
1. `cd c:\blender_installation_directory`
2. `blender -P PATH_TO_SCRIPT/discordrpblender.py`

##### Mac
Open the terminal application, go to the directory where Blender is installed, and run the executable within the app bundle, with commands like this:
1. `cd /Applications/Blender`
2. `./blender.app/Contents/MacOS/blender -P PATH_TO_SCRIPT/discordrpblender.py`

**And that's it! You'll need to run this command every time you want Discord Rich Presence for Blender.**

If you need more information visit the manual:

[Blender Manual - Command Line](https://docs.blender.org/manual/en/latest/render/workflows/command_line.html)

## Credits

Credit to [k3rn31p4nic](https://github.com/k3rn31p4nic/) for the [discoIPC](https://github.com/k3rn31p4nic/discoIPC) module for Python.

Big thanks to eKross for testing DiscordRPBlender on Windows!

## License
[CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)

