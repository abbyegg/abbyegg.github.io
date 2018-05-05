# some utility functions I've collected

def textToJsArray(filename):
    '''
    put the file in the same directory as this method
    '''
    f = open(filename, "r")
    f1 = f.readlines()
    result = "["
    for x in f1:
     result += "'"+x.rstrip()+"', "
    result = result[:-2]
    result += "]"
    print(result)