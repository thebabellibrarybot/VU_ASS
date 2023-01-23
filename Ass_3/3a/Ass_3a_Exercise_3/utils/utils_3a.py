import re
def remove_punc(text : str) -> str:
    text = (re.sub(r'[^\w\s]', '', text)).split(' ')
    return text