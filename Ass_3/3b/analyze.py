from utils import get_paths, get_basic_stats, edited_get_basic_stats
import os

input_folder = './Data/books/'

book_paths = get_paths(input_folder)

def get_book_stats(book_paths):
    """
    params
    -----
    book_paths : str
        paths to all book.txt files

    returns
    -------
    stats : dic
        dic with all stats
    """
    book2stats = {}
    for path in book_paths:
        stats = get_basic_stats(os.path.join(input_folder, path))
        book2stats[os.path.basename(path).split('.')[0]] = stats
    return book2stats

"""
un-comment below to run code and see  awnsers in terminal logs
"""
#i = get_book_stats(book_paths)
#print(i, 'book stats')



def get_book_with_highest_stats(book_stats : dict) -> dict:
    """
    params
    -----
    book_stats : dict
        dic with all books and their stats

    returns
    ------
    top_stats : dict
        dic with highest vlaue key for each stat
    """

    stats2book_with_highest_value = {}
    highest_tok = 0
    highest_sent = 0
    highest_vocab = 0
    highest_chap = 0
    for k, v in book_stats.items():
        print(k, v['num_tokens'], v['num_chaps'], v['num_sentences'], v['vocab_size'])
        if v['num_tokens'] > highest_tok:
            highest_tok = v['num_tokens']
            stats2book_with_highest_value['num_tokens'] = k

        if v['num_chaps'] > highest_chap:
            highest_chap = v['num_chaps']
            stats2book_with_highest_value['num_chaps'] = k
            
        if v['num_sentences'] > highest_sent:
            highest_sent = v['num_sentences']
            stats2book_with_highest_value['num_sentences'] = k

        if v['vocab_size'] > highest_vocab:
            highest_vocab = v['vocab_size']
            stats2book_with_highest_value['vocab_size'] = k

    return stats2book_with_highest_value

"""
un-comment below to run code and see  awnsers in terminal logs
"""
#i = get_book_with_highest_stats(i)
#print(i)

def edited_get_book_stats(book_paths):
    """
    params
    -----
    book_paths : str
        paths to all book.txt files

    returns
    -------
    stats : dic
        dic with all stats + top 30 words
    """
    book2stats = {}
    for path in book_paths:
        stats = edited_get_basic_stats(os.path.join(input_folder, path))
        book2stats[os.path.basename(path).split('.')[0]] = stats
    return book2stats

"""
un-comment below to run code and see  awnsers in terminal logs
"""
i = edited_get_book_stats(book_paths)
for k, v in i.items():
    print(k, v, 'edited')