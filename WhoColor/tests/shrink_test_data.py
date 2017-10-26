import sys
import pickle

# class TestParser(unittest.TestCase):
#     def test_whoColor_parser(self):
#         test_data = pickle.load('who_color_test_data.p')
#         for article in test_data.keys:
#             p = WikiMarkupParser(test_data[article]['rev_text'], test_data[article]['tokens'])
#             p.generate_extended_wiki_markup()
#             assert p.extended_wiki_text == test_data[article]['extended_wiki_markup']
#             assert p.present_editors == test_data[article]['present_editors']




test_data = pickle.load(open('who_color_test_data.p','rb'))

test_data_shrink = {}
i=0
count = 10
for article in test_data.keys():
	test_data_shrink[article] = test_data[article]
	
	i = i + 1
	if i >= 10 :
		break
		
pickle.dump(test_data_shrink, open('who_color_test_data_shrinked.p', 'wb'))