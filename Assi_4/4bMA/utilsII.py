import os
from utils import load_root, get_talks

def map_languages_to_paths(dir):
    lang_path = {}
    for i in os.listdir(dir):
        if i.endswith('.xml'):
            lang_path[i.replace('ted_', '').replace('-20160408.xml', '')] = os.path.join(dir, i)
    return lang_path

def find_coverage(lang_dic, num_lang = 'most'):

    """
    params
    ------
    lang_paths
        dict : dict mapping languages to paths
    most/least
        kwarg : most / least, will order dictionary from most or least talks
    
    return
    ------
    lang_len_dict
        dict : language keys with num_talks values
    """
    len_langs = {}
    for k,v in lang_dic.items():
        root = load_root(v)
        talks = get_talks(root)
        len_langs[k] = len(talks)
    if num_lang == 'most':
        return dict(sorted(len_langs.items(), key=lambda item: item[1], reverse=True))
    if num_lang == 'least':
        return dict(sorted(len_langs.items(), key = lambda item: item[1]))

def get_id_title_dict(en_path):
    """
    params
    ------
    lang_dic
        str : path to english_xml_tree
    
    returns
    -------
    talks_dic
        dic : dic of talks_ids and talk_titles
    """
    root = load_root(en_path)
    talks = get_talks(root)
    en_talks = {}
    for num, el in enumerate(talks):
        talkid = el.find('head').find('title').text
        talktitle = int(el.find('head').find('talkid').text)
        en_talks[talkid] = talktitle
    return dict(sorted(en_talks.items(), key = lambda item: item[1], reverse=True))

def map_talks_to_languages(lang_dic):
    """
    params
    ------
    lang_dic
        dic : dic mapping languages and filepaths
    
    returns
    -------
    talk_langs
        dic : dic with talk_id keys and ls of languages that include talk id as vlaue
    """
    talk_langs = {}

    for k,v in lang_dic.items():
        root = load_root(v)
        talks = get_talks(root)
        cur_lang = k
        for el in talks:
            talkid = ''
            try:
                talkid = int(el.find('head').find('talkid').text)
            except AttributeError:
                pass
            if talkid not in talk_langs:
                talk_langs[talkid] = [cur_lang]
            else:
                talk_langs[talkid].append(cur_lang)

        """
                for num, el in talks:
            
            talkid = el.find('head').find('title').text
            if talkid not in talk_langs:
                talk_langs[talkid] = [cur_lang]
            else:
                talk_langs[talkid].append(cur_lang)
        """
    return talk_langs
            
def map_nlang_to_talks(talks_lang):
    """
    params
    ------
    map_talks_to_lang
        dict : dict with talkid as key and list of langs as vlaue

    returns
    -------
    map_num_translastion
        dict : dict with num_translations as key and list of ids as value
    """
    nlag = {}
    for k, v in talks_lang.items():
        if len(v) not in nlag:
            nlag[len(v)] = [k]
        else:
            nlag[len(v)].append(k)

    return dict(sorted(nlag.items(), key = lambda item: item[1], reverse=True))

def find_top_coverage(talks_lang):

    """
    params
    ------
    lang_path
        dic : keys with talk id and value with paths
   
    return
    ------
    top_coverage
        dic : key is talk_titles by most/lease value is a list on langs talk is translated into 
    """
    
    return 'top_coverage'