import requests

#2a
# Download data on prizes
api_url = "http://api.nobelprize.org/v1/prize.json"
r = requests.get(api_url)
dict_prizes = r.json()
# uncomment the line below if you'd like to see what's inside dict_prizes
#dict_prizes 

# Download data on laureates
api_url = "http://api.nobelprize.org/v1/laureate.json"
r = requests.get(api_url)
dict_laureates = r.json()
# uncomment the line below if you'd like to see what's inside dict_prizes
#dict_laureates 

#2b
def get_laureates(dict_prizes, year = None, category = None):
    """
    parameters
    ---------
    dict_prizes : dict
        a dict of the prizes and years and stuff
    """
    
    winning_laureates = []

    for i in dict_prizes['prizes']:
        if 'laureates' not in i:
            continue
        else:
            for id in i['laureates']:
                if year != None and category != None:
                    if int(i['year']) == year:
                        if i['category'] == category:
                            if 'surname' in id and 'firstname' in id:
                                winning_laureates.append((id['firstname'] + ' ' + id['surname']))
                elif year != None and category == None:
                    print(year)                    
                    if int(i['year']) == year:
                        if 'surname' in id and 'firstname' in id:
                            winning_laureates.append((id['firstname'] + ' ' + id['surname']))
                elif year == None and category != None:
                    print(category)
                    if i['category'] == category:
                        if 'surname' in id and 'firstname' in id:
                            winning_laureates.append((id['firstname'] + ' ' + id['surname'])) 
                else:
                    print('norm')
                    if 'surname' in id and 'firstname' in id:
                        winning_laureates.append((id['firstname'] + ' ' + id['surname']))
    return winning_laureates
i = get_laureates(dict_prizes, year = 2008, category='peace')
print(i)