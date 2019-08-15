import os, shutil, random
DirToSort = ""
NameOfFiles = []
ExtOfFiles = []
end = time.time() + 10 * 15
while time.time() < end:
	for i in range(1, len(os.listdir(os.curdir))):
		if (os.path.splitext((os.listdir(os.curdir))[i])[1]) != ".ini" and (os.path.splitext((os.listdir(os.curdir))[i])[1]) != ".pyw" and (os.path.splitext((os.listdir(os.curdir))[i])[1]) != ".py":
			NameOfFiles.append(os.path.splitext((os.listdir(os.curdir))[i])[0]) 
			ExtOfFiles.append(os.path.splitext((os.listdir(os.curdir))[i])[1])
	for i in range(len(NameOfFiles)):
		if not os.path.exists(DirToSort+"\\"+ExtOfFiles[i]):
			os.mkdir(DirToSort+"\\"+ExtOfFiles[i])
		try:
			shutil.move(DirToSort+"\\"+NameOfFiles[i]+ExtOfFiles[i], DirToSort+"\\"+ExtOfFiles[i])
		except:
                        pass
