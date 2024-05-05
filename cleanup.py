import os

def RemoveFolder(folderPath):
    if os.path.exists(folderPath):
        folderContent = os.listdir(folderPath)
        for i in range(len(folderContent)):
            folderContent[i] = os.path.join(folderPath,folderContent[i])
        for file in folderContent:
            os.remove(file)
def RemoveFile(filePath):
    os.remove(filePath)
