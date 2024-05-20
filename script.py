from helper import createFolder, moveFile, findDest, cleanFile
import sys
import os

DOWNLOADS_DIR = "C:/Users/ronan/Downloads"
DOCUMENTS_DIR = "C:/Users/ronan/OneDrive/Documents"

files_downloads = os.listdir(DOWNLOADS_DIR)
files_documents = os.listdir(DOCUMENTS_DIR)

for file in files_downloads:
    file = DOWNLOADS_DIR + "/" + file

    deleted = cleanFile(file)

    if not deleted:
        destination = findDest(file)
        moveFile(file, destination)


for file in files_documents:
    file = DOWNLOADS_DIR + "/" + file

    deleted = cleanFile(file)

    if not deleted:
        destination = findDest(file)
        moveFile(file, destination)