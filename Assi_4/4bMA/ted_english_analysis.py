from utils import find_date, find_speaker, find_wc, load_root, get_talks

path = './Data/XML_releases/xml/ted_en-20160408.xml'
root = load_root(path)
talks = get_talks(root)


def find_xml_info(talk_els, len = None, time = None):
    """
    parameters
    ----------
    talks
        el : el-tree off all talk elements
    len
        kwarg : longest / shortest / None
    time
        kwarg : latest / oldest / None
    
    returns
    -------
    wc
        tup : titles, id, mean word count
    date
        tup : titles, id
    speaker
        dict : {speaker: (title, id)}
    """
    one = find_wc(talk_els, len = 'shortest')
    two = find_date(talk_els, time  = 'latest')
    three = find_speaker(talk_els)
    return  one, two, three 

i = find_xml_info(talk_els=talks)
print(i)