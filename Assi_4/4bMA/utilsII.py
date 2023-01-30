import os
from utils import load_root, get_talks

def map_languages_to_paths(dir):
    """
    param
    -----
    dir 
        str : dir
    
    result
    ------
    dic
        dic : lang name key and path value
    """
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
        talktitle = el.find('head').find('title').text
        talkid = int(el.find('head').find('talkid').text)
        en_talks[talkid] = talktitle
    return en_talks

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
        dic 
    """
    i = map_talks_to_languages(talks_lang)
        
    #i = find_top_coverage(i)
    most = 0
    least = None
    most_talk = ''
    least_talk = ''
    ml_dic = {}

    for k, v in i.items():
        if least == None:
            least = int(len(v))
        else:
            if int(len(v)) < least:
                least = int(len(v))
                talkid = k
                least_talk = (k, v)

            elif int(len(v)) > most:
                most = int(len(v))
                talkid = k
                most_talk = (k,v)

    for talk in [most_talk, least_talk]:
        new_path = './Data/XML_releases/xml/ted_{}-20160408.xml'.format(talk[1][0])
        talk_titles = get_id_title_dict(new_path)
        title = talk_titles.get(talk[0])
        ml_dic[title] = talk[1]
        
    for k, v in ml_dic.items():
        if len(v) > 1:
            print('the most translated talk is {}, which is translated into {} languages'.format(k, len(v)))
        else:
            print('the least translated talk is {}, wich is translated into {} language(s)'.format(k, len(v)))
         
    return ml_dic