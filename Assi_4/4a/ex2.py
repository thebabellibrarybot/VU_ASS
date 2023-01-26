import requests
import os
import json

#2a
api_url = "http://api.nobelprize.org/v1/prize.json"
r = requests.get(api_url)
dict_prizes = r.json()

api_url = "http://api.nobelprize.org/v1/laureate.json"
r = requests.get(api_url)
dict_laureates = r.json()


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
#print(i)

#2c
def get_affiliation_prizes(dict_laureates):

    affilliation_dic = {}

    for laur in dict_laureates['laureates']:
        for prize in laur['prizes']:
            cat_years = {}
            cat_years["category"] = prize["category"]
            cat_years["year"] = prize["year"]
            for affilliation in prize["affiliations"]:
                if type(affilliation) == list:
                    continue
                else: 
                    if affilliation["name"] in affilliation_dic:
                        affilliation_dic[affilliation["name"]].append(cat_years)
                    else:
                        affilliation_dic[affilliation["name"]] = [cat_years]
    return affilliation_dic

i = get_affiliation_prizes(dict_laureates)
#print(i)

#2d
def write_to_json(dic):

    path = './Data/json_data/NobelPrize/'
    if not os.path.exists(path):
        os.makedirs(path)


    with open('./Data/json_data/NobelPrize/nobel_prizes_affiliations.json', "w") as fi:
        
        fi.write(json.dumps(dic))

    return True

#write_to_json(i)