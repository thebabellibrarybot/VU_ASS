import pandas as pd
from nltk import tokenize as tok

tsv_path = './Data/DT_FB.csv.tsv'

#1a
def read_csv(tsv_path, delimiter = ','):
    
    df = pd.read_csv(tsv_path, sep='\t')

    csv_dic_ls = []
    for i in df.index:
        csv_dic = {}
        csv_dic['link_name'] = df['link_name'][i]
        csv_dic['num_angrys'] = df['num_angrys'][i]
        csv_dic['num_comments'] = df['num_comments'][i]
        csv_dic['num_hahas'] = df['num_hahas'][i]
        csv_dic['num_likes'] = df['num_likes'][i]
        csv_dic['num_loves'] = df['num_loves'][i]
        csv_dic['num_reactions'] = df['num_reactions'][i]
        csv_dic['num_sads'] = df['num_sads'][i]
        csv_dic['num_shares'] = df['num_shares'][i]
        csv_dic['num_wows'] = df['num_wows'][i]
        csv_dic['status_id'] = df['status_id'][i]
        csv_dic['status_link'] = df['status_link'][i]
        csv_dic['status_message'] = df['status_message'][i]
        csv_dic['status_published'] = df['status_published'][i]
        csv_dic['status_type'] = df['status_type'][i]
        csv_dic_ls.append((csv_dic))
    return csv_dic_ls

status_update = read_csv(tsv_path)
#print(i)

#1b
def get_update_most_responded_to(status_update, kwarg):
    """
    Parameters
    ----------
    status_updates:
        str : path to file with status updates
    kwarg:
        str : type of status search with terms such as
        ['likes', 'hahas', 'angrys'] 
    """

    look_for = f"num_{kwarg}"
    highest_val = 0
    status_type = ''
    status_link = ''
    status_message = ''

    for i, item in enumerate(status_update):
        focusd = int(status_update[i][look_for])
        if focusd > highest_val:
            highest_val = focusd
            status_type = status_update[i]['status_type']
            status_link = status_update[i]['status_link']
            status_message = status_update[i]['status_message']
    return status_message, status_type, status_link
#i = get_update_most_responded_to(status_update, 'hahas')
#print(i)

#1c
def get_logest_update(status_updates, length_type = "tokens"):

    df = pd.read_csv(tsv_path, sep='\t')
    longest = 0
    longest_update = ''
    for i in df.index:
        if length_type == 'tokens':
            longest_tok = tok.word_tokenize(df['status_message'][i])
            if len(longest_update) > longest:
                longest_update = df['status_message'][i]

        elif length_type == 'sentences':
            i = 'i'
        elif length_type == 'characters':
            i = 'i'
    return longest_update
#i = get_logest_update(tsv_path, 'tokens')
#print(i)