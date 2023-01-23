"""
Use your editor to create a Python script called count_words.py. Place the function definition of the my_word_count function in count_words.py. Also put a function call of the my_word_count function in this file to test it. Place your helper function definition, i.e., preprocess, in a separate script called utils_3a.py. Import your helper function preprocess into count_words.py. Test whether everything works as expected by calling the script count_words.py from the terminal.

The function preprocess preprocesses the text by removing characters that are unwanted by the user. preprocess is called within the my_word_count function and hence builds upon the output from the preprocess function and creates a dictionary in which the key is a word and the value is the frequency of the word.

Please submit these scripts together with the other notebooks.

Don't forget to add docstrings to your functions.
"""


"""
   count occurances of individual words in a string removing punctuation
   punc is removed by util script called utils_3a.py

    Parameters
    ----------
    text : str
        line of text

    Returns
    -------
    count : list
        count of unique words without punctuation 
"""
from utils import utils_3a

def my_word_counter (text : str) -> str:
    text = utils_3a.remove_punc(text)
    counter = {}

    for word in text:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

text = 'here is, well, I guess this is... like (kinda) a sentence with a word-counter. here, here, here it is I guess this is it'
i = my_word_counter(text)

print(i,'i')
