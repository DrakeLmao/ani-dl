# ani-dl: an easy to use ani-cli bulk downloader written in python

![Capture](https://github.com/user-attachments/assets/e132ebb5-3898-421e-bddb-a9c2b32724ca)

## What is the difference
ani-cli already has bulk download option but its kind of annoying to type out the command every time you want to download something so i decided to make the process easier by using a python script, it has configurationn options in the .py files which you can use to enable or disable Dub and also enable or disable default quality (you can have default quality by just not picking option during quality selector menu) also its mainly intended for termux users using android device to do their things, also you might want to change storage options if you want to save your files in a custom directory or something, you can find configuration guide below,

### Installation (Termux Android)
install the latest version of termux from fdroid: https://f-droid.org/en/packages/com.termux/
the installation instructions are given below:

Dependencies: ani-cli, python Termcolor

```pkg update -y && pkg upgrade -y && pkg install python3 ani-cli python-pip -y && pip3 install termcolor```

Lastly clone the repository:

```git clone https://github.com/DrakeLmao/ani-dl```

cd into the directly

```cd ani-dl```

run

```python3 ani.py```

if you encounter any issues try looking around the ani-cli repo
ani-cli repo: https://github.com/pystardust/ani-cli
