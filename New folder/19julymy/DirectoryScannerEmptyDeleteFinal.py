##############################################################################################
#
#  Importing required libraries
#
###############################################################################################


import sys
import os
import time
import schedule

##############################################################################################
#
# Function Header
# Function Name :       Directory Scanner
# Input :               Name odf Directory
# Description :         Deletes all empty files periodically
# Date :                19/07/2026
# Author :              Prajakta Tulshiram Sawant
#
###############################################################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40

    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")


    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : There is no such a directory with name",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name",DirectoryPath)
        return

    print("Log File gets created with name : ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("Files From the Directory are : \n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFiles = 0
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for fname in FileName:
            TotalFiles = TotalFiles + 1
            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname} : os.path.getsize {fname} bytes \n")

    
            if(os.path.getsize{fname} == 0)
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)



    fobj.write(Border+"\n")
    fobj.write("Total files scanned : {TotalFiles}\n")
    fobj.write("Total empty files found and delete : {EmptyFiles} \n")
    fobj.write(Border+"\n")
    fobj.write("Log File gets created at : "+timestamp)       
    fobj.write("\n"+Border+"\n")

    fobj.close()

##############################################################################################
#
# 
# Function Name :       Main
# Input :               Command line arguments
# Description :         it controls the script
# Date :                19/07/2026
# Author :              Prajakta Tulshiram Sawant
#
###############################################################################################

def main():
    Border = "-"*40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)   

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is use to traverse directory")
            print("For better usage please check --u flag")
           
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:

            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)


    else:
        print("Invalid number of arguments..")
        print("Please use --h or --u for more information..")
        
    print(Border)
    print("Thank You For Using Marvellous Automation Script")
    print(Border)

##############################################################################################
#
#  Starter of the Automation Script
#
###############################################################################################

if __name__ == "__main__":
    main()
   

   #error