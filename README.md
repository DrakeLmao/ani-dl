# ani-dl: an easy to use ani-cli bulk downloader and wrapper written in python

![Capture](https://github.com/user-attachments/assets/e132ebb5-3898-421e-bddb-a9c2b32724ca)

## What is the difference?
ani-cli already has bulk download option but its kind of annoying to type out the command every time you want to download something so i decided to make the process easier by making a wrapper using python, it has configurationn options in the .py files which you can use to enable or disable Dub and also enable or disable default quality (you can have default quality by just not picking option during quality selector menu) also its mainly intended for termux users using android device to do their things, also you might want to change storage options if you want to save your files in a custom directory or something, you can find configuration guide below,

## Installation (Termux Android)
install the latest version of termux from fdroid: https://f-droid.org/en/packages/com.termux/
the installation instructions are given below:

Dependencies: ani-cli, python Termcolor

```pkg update -y && pkg upgrade -y && pkg install python3 ani-cli git python-pip -y && pip3 install termcolor```

Lastly clone the repository:

```git clone https://github.com/DrakeLmao/ani-dl```

cd into the directly

```cd ani-dl```

run

```python3 ani.py```

if you encounter any issues try looking around the ani-cli repo
ani-cli repo: https://github.com/pystardust/ani-cli

## Configuration:
Behind all that spaghetti code ani-dl comes with three distinct configuration options:

![Capture](https://github.com/user-attachments/assets/d09be15e-824b-45a2-a914-bbcb1d63d4e4)

```StoreOnInternal``` this option enables you to store your downloaded media to any folder in your device

Note: for termux users you must grant storage permission by typing ```termux-setup-storage``` beforehand on the app, its False by default. if your desired storage location is somewhere else you can change it to your liking.

```Defaultquality``` Disables QualitySelector in exchange for Default quality selected by ani-cli, its False by default

```Dub``` Enables Dub, set this to False if you want to download with subs

### Changing save location

![Capture](https://github.com/user-attachments/assets/9cfc3a05-336a-4d64-823b-5c8c9447148d)

inside the .py file there's a Save location option, set it to your desired location and it should download on the location, make sure the path is legit, after typing desired storage location set SaveOnInternal to true
