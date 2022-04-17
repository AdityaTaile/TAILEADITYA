import os
import sys
import re

def filenames_in_script_folder():
    """
    Returns all the filenames which are located in the same folder
    as this running python script
    """
    os.chdir(os.path.dirname(sys.argv[0]))
    return os.listdir(os.getcwd())


def words_from_file(filename):
    """
    Reads text file and returns all the words in it
    """
    file = open(filename)
    file_content = file.read()
    file.close()
    return file_content.split()


def ask_for_replace_word(keyword):
    """
    Asks for a replace for mentioned keyword.
    Checks if keyword is a vowel to follow english grammar correct
    """
    vowel_regex = re.compile('^[aeiou]')
    if vowel_regex.search(keyword):
        return input("Enter an " + keyword.lower() + "\n")
    return input("Enter a " + keyword.lower() + "\n")


def replace_word(word, keywords):
    """
    Replaces provided word if it matches with one of the keywords.
    Any non alphabetical signs are ignored in keyword compare
    Otherwise returns provided word
    """
    no_char_regex = re.compile('[^a-zA-Z]')
    clean_word = no_char_regex.sub('', word)

    for keyword in keywords:
        if clean_word == keyword:
            new_word = ask_for_replace_word(keyword)
            return word.replace(keyword, new_word)
    return word


def write_data_to_file(data, filename):
    """
    Writes provided data to file.
    If no file exists a new one is created first
    """
    file = open(filename, 'w')
    file.write(data)
    file.close()


def mad_libs():
    """
    Main function reads from file, replaces keywords
    and writes to new file
    """
    for filename in filenames_in_script_folder():
        if filename.lower().endswith('.txt'):
            new_words = []
            replaced_a_word = False

            for word in words_from_file(filename):
                KEYWORDS = ('ADJECTIVE', 'NOUN', 'VERB', 'ADVERB')
                replace = replace_word(word, KEYWORDS)
                if replace != word:
                    replaced_a_word = True
                new_words.append(replace)

            if replaced_a_word:
                new_data = ' '.join(new_words)
                print(new_data)
                write_data_to_file(new_data, filename[:-4] + "_mad.txt")

mad_libs()