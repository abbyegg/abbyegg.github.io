# some utility functions I've collected
import sys

def textToJsArray(filename):
    '''
    put the file in the same directory as this method
    '''
    f = open(filename, "r")
    f1 = f.readlines()
    result = "["
    for x in f1:
     result += "'"+x.rstrip().capitalize()+"', "
    result = result[:-2]
    result += "]"
    print(result)

def main():
    for arg in sys.argv:
        textToJsArray(arg)

if __name__ == "__main__":
    main()