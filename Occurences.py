import os
import sys
      
def count_occurences_in_file( filepath ):  
    if not os.path.isfile(filepath):
        raise Exception('Path ' + os.path.join(os.getcwd(),filepath) + ' is not a file')
    with open(filepath, 'r') as file_object:
        return count_occurences(file_object.read())

def count_occurences( content ):
    return dict( (char, content.count(char)) for char in set(content) )
