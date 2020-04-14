import os, glob

def changeFileExtensionForAllFilesinDirectory(folder_path):
    os.chdir(folder_path)
    for fi in glob.glob("*.cvs"):
        os.rename(fi, fi[:-3] + "csv")  