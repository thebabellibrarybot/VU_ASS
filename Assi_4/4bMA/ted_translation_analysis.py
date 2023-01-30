from utilsII import find_coverage, map_languages_to_paths, get_id_title_dict, map_talks_to_languages, map_nlang_to_talks, find_top_coverage

path = './Data/XML_releases/xml/'
en_path = './Data/XML_releases/xml/ted_en-20160408.xml'

lang_path = map_languages_to_paths(path)

i = find_coverage(lang_path, 'most')

i = get_id_title_dict(en_path)
#print(i)

i = map_talks_to_languages(lang_path)

i = map_nlang_to_talks(i)

i = find_top_coverage(lang_path)
    

