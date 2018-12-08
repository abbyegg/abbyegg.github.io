# some utility functions I've collected
import sys

def textToJsArray(filename):
    '''
    put the file in the same directory as this method
    '''
    f = open(filename, "r")
    lines = f.readlines()
    result = "["
    for line in lines:
     # result += "'"+x.rstrip().capitalize()+"', "
     result += "'" + line.rstrip() + "', "
    result = result[:-2]
    result += "]"
    print(result)

def main():
    for arg in sys.argv:
        textToJsArray(arg)

if __name__ == "__main__":
    main()