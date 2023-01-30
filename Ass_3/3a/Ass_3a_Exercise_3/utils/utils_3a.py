import re
def preprocess(text : str) -> str:
    text = (re.sub(r'[^\w\s]', '', text)).split(' ')
    return text