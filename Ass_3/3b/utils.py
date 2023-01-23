import os
from nltk import tokenize as tok
import re

def get_paths(input_folder : str) -> str:
    file_ls = []
    for file in os.listdir(input_folder):
        file_ls.append(file)
    return file_ls

def get_basic_stats(book_path : str) -> str:

    # num of sentences

    # num of tokens

    # size of vocabulary i.e. unique tokens

    # occurances of CHAPTER in huck, Chapter in anna, ACT in macbeth

    stat_dic = {}

    with open(book_path, 'r') as cur_book:
        num_sentences = 0
        num_tokens = 0
        num_chaps = 0
        vocab = []
        for sent in tok.sent_tokenize(cur_book.read()):
            num_sentences += 1 
            tokens = tok.word_tokenize(sent)
            for token in tokens:
                num_tokens += 1
                vocab.append(token)
                if token == 'CHAPTER' and os.path.basename(book_path).split('.')[0] == 'HuckFinn':
                    num_chaps += 1
                elif token == 'Chapter' and os.path.basename(book_path).split('.')[0] == 'AnnaKarenina':
                    num_chaps += 1
                elif token == 'ACT' and os.path.basename(book_path).split('.')[0] == 'Macbeth':
                    num_chaps += 1
        stat_dic['num_sentences'] = num_sentences
        stat_dic['num_tokens'] = num_tokens
        stat_dic['num_chaps'] = num_chaps
        stat_dic['vocab_size'] = len(set(vocab))

    return stat_dic

def edited_get_basic_stats(book_path : str) -> str:
    # num of sentences

    # num of tokens

    # size of vocabulary i.e. unique tokens

    # occurances of CHAPTER in huck, Chapter in anna, ACT in macbeth

    # top_30_tokens
    stat_dic = {}

    with open(book_path, 'r') as cur_book:
        num_sentences = 0
        num_tokens = 0
        num_unique_tokens = {}
        num_chaps = 0
        vocab = []
        top_30_tokens = []
        for sent in tok.sent_tokenize(cur_book.read()):
            num_sentences += 1 
            tokens = tok.word_tokenize(sent)
            for token in tokens:
                token = re.sub(r'[^\w\s]','',token)
                num_tokens += 1
                vocab.append(token)
                if token not in num_unique_tokens:
                    num_unique_tokens[token] = 1
                if token in num_unique_tokens:
                    num_unique_tokens[token] += 1
                if token == 'CHAPTER' and os.path.basename(book_path).split('.')[0] == 'HuckFinn':
                    num_chaps += 1
                elif token == 'Chapter' and os.path.basename(book_path).split('.')[0] == 'AnnaKarenina':
                    num_chaps += 1
                elif token == 'ACT' and os.path.basename(book_path).split('.')[0] == 'Macbeth':
                    num_chaps += 1
        for k, v in sorted(num_unique_tokens.items(), key = lambda x: x[1], reverse = True)[:30]:
            top_30_tokens.append(k)
            with open(os.path.join('./Data/out', os.path.basename(book_path)), 'a+') as new_fi:
                new_fi.write(k + ', '+ str(v))
                new_fi.write('\n')



        stat_dic['num_sentences'] = num_sentences
        stat_dic['num_tokens'] = num_tokens
        stat_dic['num_chaps'] = num_chaps
        stat_dic['vocab_size'] = len(set(vocab))
        stat_dic['top_30_tokens'] = top_30_tokens


    return stat_dic