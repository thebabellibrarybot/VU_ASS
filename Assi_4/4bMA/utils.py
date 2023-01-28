from lxml import etree as et
import numpy as np
from datetime import date as d8


# what is the longest and shortest talk, what is the avg word count
def find_wc(talk_els, len = None):
    n_talks = 0
    n_talks_short = 0
    n_talks_long = 0
    avg = []
    ids_short = ''
    ids_long = ''
    #longest = 'Longest talk: {n_talks} '
    #shortest = 'Shortest len: {n_talks_short}'
    #avg = 'Avg talk len: {avg_len}'
    for num, el in enumerate(talk_els):
        n_talks += 1
        wordnum = int((el.find('head').find('wordnum')).text)
        title_id = (el.find('head').find('title').text, el.find('head').find('talkid').text)
        avg.append(wordnum)
        if n_talks <= 1:
            n_talks_long = wordnum
            n_talks_short = wordnum
        if n_talks > 1:
            if wordnum < n_talks_short:
                n_talks_short = wordnum
                ids_short = title_id
            if wordnum > n_talks_long:
                n_talks_long = wordnum
                ids_long = title_id
    avg_len =  np.mean(avg)
    
    if len == None:
        print('Avg talk len: {}'.format(avg_len))
        print('Longest talk: {}'.format(ids_long))
        print('Shortest talk: {}'.format(ids_short))
        print('Num talks: {}'.format(n_talks))
        return ids_long, ids_short
    elif len == 'longest':
        print('Avg talk len: {}'.format(avg_len))
        print('Longest talk: {}'.format(ids_long))
        print('Num talks: {}'.format(n_talks))
        return ids_long
    elif len == 'shortest':
        print('Avg talk len: {}'.format(avg_len))
        print('Shortest talk: {}'.format(ids_short))
        print('Num talks: {}'.format(n_talks))
        return ids_short

# what is the oldest and latest talk
def find_date(talk_els, time = 'latest'):

    date = 0
    date_time = 0
    ids = ''
    month_mapping = {
    "jan": '1',
    "feb": '2',
    "mar": '3',
    "apr": '4',
    "may": '5',
    "jun": '6',
    "jul": '7',
    "aug": '8',
    "sep": '9',
    "oct": '10',
    "nov": '11',
    "dec": '12'
}
    for num, el in enumerate(talk_els):

        dtime = el.find('head').find('dtime').text
        title_id = (el.find('head').find('title').text, el.find('head').find('talkid').text)
        
        if num < 1:

            date = d8(int(dtime.split(' ')[5]), int(month_mapping[(dtime.split(' ')[1]).lower()]), int(dtime.split(' ')[2]))
            date_time = dtime.split(' ')[3]

        if num > 0:

            cur_date = d8(int(dtime.split(' ')[5]), int(month_mapping[(dtime.split(' ')[1]).lower()]), int(dtime.split(' ')[2]))

            if time == 'latest':
                if cur_date > date:
                    date = cur_date
                    date_time = dtime.split(' ')[3]
                    ids = title_id
                elif cur_date == date:
                    cur_date_time = dtime.split(' ')[3]
                    if cur_date_time[0:5] > date_time[0:5]:
                        date = cur_date
                        date_time = cur_date_time
                        ids = title_id
                    
            elif time == 'oldest':
                if cur_date < date:
                    date = cur_date
                    date_time = dtime.split(' ')[3]
                    ids = title_id
                elif cur_date == date:
                    cur_date_time = dtime.split(' ')[3]
                    if cur_date_time[0:5] < date_time[0:5]:
                        date = cur_date
                        date_time = cur_date_time
                        ids = title_id
                    
    print('the {} element is: {}'.format(time, ids))
    return ids

# who spoke more than once
def find_speaker(talk_els):

    multi_speakers = {}

    for num, el in enumerate(talk_els):
        speaker = el.find('head').find('speaker').text
        if speaker in multi_speakers:
            multi_speakers[speaker].append((el.find('head').find('title').text, el.find('head').find('talkid').text))
        else:
            multi_speakers[speaker] = [(el.find('head').find('title').text, el.find('head').find('talkid').text)]

    filted_dict = {k:v for k, v in multi_speakers.items() if len(v) >= 2}
    
    return filted_dict


# load xml el
def load_root(path):
    tree = et.parse(path)
    root = tree.getroot()
    return root
def get_talks(root):
    
    talks = root.findall('file')
    return talks

#TODO change defs so that 
# def loop() -> loops through talk_els
# def find_XX() -> finds x for item in loop
# returns all info with a single loop cycle
# i.e.
# def loop(talk_els)
# speakers, dates, wc = '', '', ''
# for num, el in enumerate(talk_els):
#   speakers = find_speakers(el)
#   ...