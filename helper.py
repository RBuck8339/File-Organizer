import os
import string
import shutil

DOWNLOADS_DIR = "C:/Users/ronan/Downloads"
DOCUMENTS_DIR = "C:/Users/ronan/OneDrive/Documents"
SCHOOL_DIR = 'C:/Users/ronan/Downloads/School'


CLASSES_DICT = {"Fall 2021": ["MUL2010", "IDH1930", "ENC1101", "EVR1001C", "MAC2311"], 
                "Spring 2022": ["COP1500", "ARH2000", "ENC1102", "MAC2312", "HUM1020"],
                "Fall 2022": ["CHM1045", "COP2006", "MAD3107", "STA2023"],
                "Spring 2023": ["COP3003", "PHY2048", "JROTC", "MAC2313", ], 
                "Fall 2023": ["COP3223H", "SPC1603H", "ENC3241", "COT3100C", "IDH1920H"],
                "Spring 2024": ["COP3502H", "CIS3360", "COP3330", "CDA3103"]
            }

UNIVERSITY_DICT = {"UCF": ["UH", "UCF", "BHC", "Honors"],
                   "FGCU": ["FGCU", "ACE", "Collegiate"]
                }

TO_DELETE = ["RonanBuck Resume ("]

HOUSING = ["lease", "Retreat"]

SETUP_INSTALLERS = ["Setup", "Installer"]

MODS = ["Elden", "Mod", "Pokemon", "randomizer", "Randomizer"]

def createFolder(path: string):
    pass


def findDest(file, type):
    for semester in CLASSES_DICT.keys():
        for course in CLASSES_DICT[semester]:
            if course in file:
                return SCHOOL_DIR + "/Schoolwork/" + semester + "/" + course
            
    for university in UNIVERSITY_DICT.keys():
        for topic in UNIVERSITY_DICT[university]:
            if topic in file:
                return SCHOOL_DIR + "/" + topic
            
    for item in HOUSING:
        if item in file:
            return "C:/Users/ronan/Downloads/Retreat West"

    if "CoverLetter" in file:
        return "C:/Users/ronan/Downloads/Cover Letters"
            
    for item in MODS:
        if item in file:
            return "C:/Users/ronan/Downloads/Mods"
        
    for item in SETUP_INSTALLERS:
        if item in file:
            return "C:/Users/ronan/Downloads/SetupInstallers"
    

    return "Not_Available"
        

def moveFile(file, dest):
    if dest != "Not_Available":
        try:
            shutil.move(file, dest)
        except:
            cleanFile(file)


def cleanFile(file):
    for name in TO_DELETE:
        if name in file:
            os.remove(file)
            return True
    