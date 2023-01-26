import zipfile, os

def iteratingFolders():
    for folderName, subfolders, filenames in os.walk('/home/rcolejnr/IdeaProjects/automate stuff/code/automating tasks'):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            for filename in filenames:
                print('FILE INSIDE ' + folderName + ': '+ filename)
        print('')
def zippingFiles():
    os.chdir('/home/rcolejnr/Документы/Coding/Python/Automate_the_Boring_Stuff_onlinematerials') # move to the folder with file.zip
    egZip = zipfile.ZipFile('example.zip')
    print(egZip.namelist())
    # ls zip files
    spamInfo = egZip.getinfo('spam.txt')
    spamInfo.file_size
    print(spamInfo.compress_size)
    egZip.close()
