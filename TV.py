import os

programList = []
seasonList = []
episodeList =[]
program = ""
downloadsFolder = "C:/Users/edwar/Downloads/"

for fileName in os.listdir(downloadsFolder):
    if "Season" in fileName and fileName.split("Season")[0] not in programList:
        programList.append(fileName.split("Season")[0])

for i in range(len(programList)):
    print(str(i + 1) + ": " + programList[i])

        
print("Select Program:")
program = programList[int(input()) - 1]


for folderName in os.listdir(downloadsFolder):
    if program in folderName:
        seasonList.append(folderName)

print("Select Season:")
for i in range(len(seasonList)):
    print(str(i + 1) + ": " + seasonList[i])

seasonFolder = downloadsFolder + "/" + seasonList[int(input()) - 1]

for fileName in os.listdir(seasonFolder):
    episodeList.append(fileName)

print("Select Episode:")
for i in range(len(episodeList)):
    print(str(i + 1) + ": " + episodeList[i])

episode = seasonFolder + "/" + episodeList[int(input()) - 1]
os.startfile(episode)


