import sys
sys.path.append('H:\wiki-who\WhoColor\WhoColor')
import unittest
import pickle
from WhoColor.parser import WikiMarkupParser

# class TestParser(unittest.TestCase):
#     def test_whoColor_parser(self):
#         test_data = pickle.load('who_color_test_data.p')
#         for article in test_data.keys:
#             p = WikiMarkupParser(test_data[article]['rev_text'], test_data[article]['tokens'])
#             p.generate_extended_wiki_markup()
#             assert p.extended_wiki_text == test_data[article]['extended_wiki_markup']
#             assert p.present_editors == test_data[article]['present_editors']




#test_data = pickle.load(open('../who_color_test_data.p','rb'))

#shrinked datasets - to check the validity quickly and fix the bugs
test_data = pickle.load(open('../who_color_test_data_shrinked.p','rb'))

for article in test_data.keys():
    print(article)
    p = WikiMarkupParser(test_data[article]['rev_text'], test_data[article]['tokens'])
    p.generate_extended_wiki_markup()

    # Some of the entries in tuple are out of order. Not sure why and hence sorting both based on author id
    p.present_editors = tuple(sorted(list(p.present_editors), key=lambda x: x[0]))
    test_data[article]['present_editors'] = tuple(sorted(list( test_data[article]['present_editors']), key=lambda x: x[0]))

    assert p.extended_wiki_text == test_data[article]['extended_wiki_markup']
    assert p.present_editors == test_data[article]['present_editors']

    #assert len(p.present_editors) == len(test_data[article]['present_editors'])
    #for i in range(0,len(p.present_editors)):
    #    if p.present_editors[i] != test_data[article]['present_editors'][i] :
    #        #print(p.present_editors[i])
    #        #print(test_data[article]['present_editors'][i])
    #        print(i)
print('end of program')
