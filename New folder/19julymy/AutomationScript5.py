#python Automation.py --h
#python Automation.py --u
#python Automation.py Marvellous

#python Automation.py --d
#python Automation.py Marvellous Demo




import sys


def main():
    print("--------------------------------------------------------------------------")
    print("Marvellous Infosystems")
    print("--------------------------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is use to traverse directory")
            print("For better usage please check --u flag")
           
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("DirectoryName name is : ",DirectoryName)

    else:
        print("Invalid number of arguments..")
        print("Please use --h or --u for more information..")

    print("--------------------------------------------------------------------------")
    print("Thank You For Using Marvellous Automation Script")
    print("--------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
    #error