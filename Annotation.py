
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path
from termcolor import colored


PICTURE_PATH = ""
INPUT_PATH = ""
OUTPUT_PATH = ""

#PICTURE_PATH = r'C:\Users\paulb\Desktop\Bosch Programm\1\img'
#INPUT_PATH = r'C:\Users\paulb\Desktop\Bosch Programm\1\AnnotationText.txt'
#OUTPUT_PATH = r'C:\Users\paulb\Desktop\Bosch Programm\1\AnnotationTextNew.txt'

Input_Values = []
Output_Values = []

the_file = None


def main():

    getAllPaths()
    loadText()

    Iteration(getStartLine())

#works
def getAllPaths():

    global PICTURE_PATH
    global INPUT_PATH
    global OUTPUT_PATH

    PICTURE_PATH = getPath("directory", "Picture Folder Path")

    INPUT_PATH = getPath("file", "Input Text Path")

    print("Give Path of Output Text Path. If file already exist, it will be overwritten.")
    OUTPUT_PATH = Path(input().replace("\\" ,"/"))

def getPath(p_type, p_name): #p_type must be either "directory" or "file"
    print("Give path of " + p_name)
    temp = input()
    ret = Path(temp.replace("\\","/"))
    if(p_type == "directory"):
        if not(os.path.isdir(ret)):
            print("Path is no directory. Please insert directory path.")
            return getPath(p_type,p_name)
    else:
        if(p_type == "file"):
            if not(os.path.isfile(ret)):
                print("Path is no file. Please insert File Path.")
                return GetPath(p_type,p_name)

        else:
            print("Path could not be recognized as a Path or file. Please change Path structure to a similar to  C:\\Users\\paulb\\Downloads ")
            return GetPath(p_type,p_name)
    return ret



#works
def loadText():
    global INPUT_PATH

    Input_file = open(INPUT_PATH,"r")
    lines = Input_file.readlines()

    for line in lines:
        temp = line.split(";")
        while len(temp) < 3:
            temp.append("")

        Input_Values.append(temp)



def print2DimArr(p_arr):

    for a in p_arr:
        for b in a:
            print(b)


def Iteration(p_StartLine):
    output = open(OUTPUT_PATH,"w+")
    i = p_StartLine -1
    while i < len(Input_Values):
        print("Bild: " + Input_Values[i][0])
        print("Current Value: " )
        print("----------------------")
        print(" ")
        print(Input_Values[i][2])
        print(" ")
        print("----------------------")

        toWrite = ""
        try:
            img = mpimg.imread(PICTURE_PATH / Input_Values[i][0])
            plt.imshow(img)
            plt.axis("off")



            plt.show(block = False)
            plt.pause(0.1)
            temp = input()
            plt.close('all')



            if (temp == "stop"):
                print("Start next time at line :" + str(i + 1))
                break
            if (temp == "."):  # alte Value, Zeile 3 der iput, übernehmen
                temp = Input_Values[i][2]
            if (temp == "back"):
                i = i - 1
                del Output_Values[-1]
                continue
            # writeToFile(Input_Values[i][0] , Input_Values[i][1] , temp) this was the old way with writeToFile()
            toWrite = str(Input_Values[i][0]) + ";" + str(Input_Values[i][1]) + ";" + str(temp)
        except FileNotFoundError:
            print(colored("File " + Input_Values[i][0] + " not found in the given picture directory. Moving on to next line.","red"))
        except:
            print("unexpected error while opening picture file. Check file paths and access.")




        Output_Values.append(toWrite)
        i += 1
    writeToFileFromArray()
    print("Annotation finished")


#outdated , was line by line
def writeToFile(p_a, p_b ,p_c):

    tempText = p_a + ";" + p_b + ";" + p_c
    the_file = open(OUTPUT_PATH, 'a')
    the_file.write(tempText + '\n')

def writeToFileFromArray():
    the_file = open(OUTPUT_PATH, 'a')
    for s in Output_Values:
        the_file.write(s + '\n')


def getStartLine():
    print("Start at Line:")

    try:
        ret = int(input())
        return ret
    except Exception:
        print("must be a number.")
        return getStartLine()





main()