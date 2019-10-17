import os, time, shutil
# imports the modules needed
DirToSort = ""
# sets an empty str var to store the dir
NameOfFiles = []
# sets and empty list to store the names of files
ExtOfFiles = []
# sets and empty list to store the names and extentions of files
self_file = os.path.basename(__file__)
# finds this file so that it doesnt sort itself
end = time.time() + 10 * 15
while time.time() < end: # repeat for the next 10^15 seconds
	for i in range(1, len(os.listdir(os.curdir))): # for every item in the current dir
		if (os.path.splitext((os.listdir(os.curdir))[i])[1]) != ".ini": # if the item ends doesnt end in .ini
			#this checks if the file is a .ini (windows file) because this doesnt need to move 
			NameOfFiles.append(os.path.splitext((os.listdir(os.curdir))[i])[0])  # adds the Name of the file into the NameOfFiles list
			ExtOfFiles.append(os.path.splitext((os.listdir(os.curdir))[i])[1]) # adds the Name and Extention of the file into the ExtOfFiles list
	for i in range(len(NameOfFiles)): # for every item in the list of NameOfFiles
		if not os.path.exists(DirToSort+"\\"+ExtOfFiles[i]): # if the dir already exists
			os.mkdir(DirToSort+"\\"+ExtOfFiles[i]) # make the directory
		try: # try the code below
			shutil.move(DirToSort+"\\"+NameOfFiles[i]+ExtOfFiles[i], DirToSort+"\\"+ExtOfFiles[i]) # move the file into the corisponding folder
		except: # if the above code returns an error then pass from the loop
                        pass
