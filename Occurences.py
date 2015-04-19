import os
import sys

#Return dict of character count      
def characters( content ):
    return dict( (char, content.count(char)) for char in set(content) )

#Return dict of count of each substring in a set
def substrings( content, string_set ):
    return dict( (string, content.count(string)) for string in string_set )

#Return dict of count of unique words
def words( content, delimiter = " " ):
    return dict( (char, content.count(char)) for char in set(content.split(delimiter)) )

#Read in file content
def _read_file_input( filepath ):
    if not os.path.isfile(filepath):
        raise Exception('Path ' + os.path.join(os.getcwd(),filepath) + ' is not a file')
    with open(filepath, 'r') as file_object:
        return file_object.read()

#Return dict of character count in text file
def characters_in_file( filepath ):
    content = _read_file_input(filepath)
    return characters(content)

#Return dict of count of each substring in a set, in a text file 
def substrings_in_file( filepath, string_set ):
    content = _read_file_input(filepath)
    return substrings(content,string_set)

#Return a dict of count of unique words in a text file
def words_in_file( filepath, delimiter = " " ):
    content = _read_file_input(filepath)
    return words(content,delimiter)

