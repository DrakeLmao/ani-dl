# ani-dl: an easy to use ani-cli bulk downloader and wrapper written in python

![Capture](https://github.com/user-attachments/assets/e132ebb5-3898-421e-bddb-a9c2b32724ca)

## What is the difference?
ani-cli already has bulk download option but its kind of annoying to type out the command every time you want to download something so i decided to make the process easier by making a wrapper using python, it has configurationn options in the .py files which you can use to enable or disable Dub and also enable or disable default quality (you can have default quality by just not picking option during quality selector menu) also its mainly intended for termux users using android device to do their things, also you might want to change storage options if you want to save your files in a custom directory or something, you can find configuration guide below,

## Installation (Termux Android)
install the latest version of termux from fdroid: https://f-droid.org/en/packages/com.termux/
the installation instructions are given below:

Dependencies:
1. ani-cli
2. python
3. termcolor
4. pip
5. ani-cli's dependencies to run ani-cli. If you cannot install all of ani-cli's dependencies, at least try and get these:
    - grep
    - sed
    - curl
    - fzf
    - aria2c

          pkg update -y && pkg upgrade -y && pkg install grep sed curl wget fzf aria2 python ani-cli git python-pip -y && pip3 install termcolor

Lastly clone the repository and cd into the directory:

    git clone https://github.com/DrakeLmao/ani-dl && cd ani-dl
run

    chmod +x ani-dl && mv ani-dl /data/data/com.termux/files/usr/bin && cd .. && rm -rf ani-dl && ani-dl

now you can finally run ani-dl by typing
 
    ani-dl

##### Uninstallation:
to uninstall ani-dl type:

     rm /data/data/com.termux/files/usr/bin/ani-dl

if you encounter any issues try submitting an issue

## Configuration:
Behind all that spaghetti code ani-dl comes with three distinct configuration options:

![Capture](https://github.com/user-attachments/assets/d09be15e-824b-45a2-a914-bbcb1d63d4e4)

```StoreOnInternal``` this option enables you to store your downloaded media to any folder in your device

Note: for termux users you must grant storage permission by typing ```termux-setup-storage``` beforehand on the app, its False by default. if your desired storage location is somewhere else you can change it to your liking.

```Defaultquality``` Disables QualitySelector in exchange for Default quality selected by ani-cli, its False by default

```Dub``` Enables Dub, set this to False if you want to download with subs

### Changing Configuration Options:
to change configuration options you must clone this repository and cd into the repo:
 
    git clone https://github.com/DrakeLmao/ani-dl && cd ani-dl

now use any cli text editor (i personally use vim but you can try nano)

    nano ani-dl

great now you can change configuration options, once you find it to your liking install ani-dl on termux by typing

    chmod +x ani-dl && mv ani-dl /data/data/com.termux/files/usr/bin && ani-dl


#### Changing save location

![Capture](https://github.com/user-attachments/assets/9cfc3a05-336a-4d64-823b-5c8c9447148d)

inside the ani-dl file there's a Save location option, set it to your desired location and it should download on the location, make sure the path is legit, after typing desired storage location set SaveOnInternal to true
