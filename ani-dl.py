from termcolor import colored
import os
line = ("----------------------")
print(colored(line, 'blue'))
print(colored("Ani-Cli Client Revamped", 'red'))
print(colored(line, 'green'))
print()

def Config():
  global StoreOnInternal
  global DefaultQuality
  global Dub
  #Variables, Set these to true or false
  StoreOnInternal = False
  DefaultQuality = False
  Dub = True

def ReadConfig(): 
    global selectedquality
    global SaveLocation
    global DubVar
    #Quality
    if DefaultQuality == True:
        selectedquality = ''
    else:
        DownloadQualitySelector()
    #SaveLocation
    if StoreOnInternal == True:
        SaveLocation = "/sdcard/ani-cli"
    else:
        SaveLocation = ""
    #DubFunction
    if Dub == True:
        DubVar = "--dub"
    else:
        DubVar = ""

def DownloadQualitySelector():
    global selectedquality
    print(colored('Please select your quality', 'green'))
    print("1 = 1080p")
    print("2 = 720p")
    print("3 = 480p")
    print("4 = 360p")
    qualityno = input(colored('Quality: ', 'red'))
    if qualityno == "":
        selectedquality = ''
    if qualityno == "1":
        selectedquality = "-q 1080p"
    if qualityno == "2":
        selectedquality = "-q 720p"
    if qualityno == "3":
        selectedquality = "-q 480p"
    if qualityno == "4":
        selectedquality = "-q 360p"

def EpisodeRangeMapper():
    global Range1 
    global Range2
    global Episode_Range
    print()
    print(colored(line, 'blue'))
    print(colored('  Episode Selector', 'red'))
    print(colored(line, 'green'))
    print()
    Range1 = input(colored("Pick First EP in range: ", 'yellow'))
    Range2 = input(colored("Pick second EP in range: ", 'yellow'))
    print()
    print(colored(line, 'blue'))
    Episode_Range = (f'-e "{Range1} {Range2}"')

def CommandRunner():
    global Command
    AniCommand = (f'ani-cli {DubVar} {Episode_Range} {selectedquality} -d')
    SaveCommand = (f'cd {SaveLocation}')
    Command = (f'{SaveCommand} && {AniCommand}')
    os.system(Command)

def InfoMenu():
    print(colored(line, 'blue'))
    print(colored('   Information Menu', 'green'))
    print(colored(line, 'red'))

    if selectedquality == '':
      print(colored("[INFO] DefaultQuality config is set to true, proceeding to Download [INFO]", 'magenta'))
    if DubVar == '':
        print(colored("[INFO] Dub config is set to false, proceeding to Download With Dub disabled [INFO]", 'magenta',))
    else:
        print(colored("[INFO] Dub config is set to true, proceeding to Download With Dub enabled [INFO]", 'magenta'))
 
def RunnerScript():
    Config()
    ReadConfig()
    InfoMenu()
    EpisodeRangeMapper()
    CommandRunner()
    #Debug()

def Debug():
    print (f"Range1 = {Range1} Range2 = {Range2} Quality = {selectedquality} Dub = {DubVar}, Save Location = {SaveLocation} Command = {Command}")
#Execute
RunnerScript()
