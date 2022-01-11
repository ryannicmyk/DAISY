# This is Daisy. i saw a program at the exporitorium in SF that was titled the same name, and it was a chatbot that
# would learn as you talked to it. i wanna make a program similar as i cant find it anywhere on the internet. all i
# can find is some twitter posts of people interacting with it, and this pdf explaning the concept from 2007:
# https://www.exploratorium.edu/files/vre/pdf/daisy2_rp_02.pdf
import os
import markovify as mv
from colorama import Fore

# Input Text File
InputText = "testmateral/Lee.txt"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def printn(out):
    if out is None:
        print(Fore.GREEN + "DAISY Could not produce a meaningful response.")
    else:
        print(Fore.GREEN + "DAISY>>>" + out)


with open(InputText) as f:
    InputFile = f.read()
# Random Sentance structure vocab that is grammaticlly correct but makes no sense
with open("Vocab.txt") as b:
    VocabFile = b.read()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate(data):
    with open('tempcore.txt', 'a') as hs:
        if data is None:
            printn("")
        else:
            hs.write(data + "\n")
    with open("tempcore.txt") as data1:
        corefile = data1.read()
    Input_model = mv.NewlineText(InputFile, well_formed=False)
    Vocab_model = mv.NewlineText(VocabFile, well_formed=False)
    coremodel = mv.NewlineText(corefile, well_formed=False)
    # Responce is based on InputText, the sample Vocab file, and user inputted text with a heavy weight on the first
    # and the last
    outmodel = mv.combine([Input_model, Vocab_model, coremodel], [2, 1, 5], )
    return outmodel


# Inital start
Username = input("Enter a name: ")
cls()
printn(" Hello " + Username)
while True:
    # Data Repeator
    usr = input(Username + ">>> ")
    while True:
        output = (generate(usr).make_sentence())
        if output is not None:
            break
    printn(output)
