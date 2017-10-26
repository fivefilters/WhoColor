if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    print(path.dirname(path.dirname(path.abspath(__file__))))

import pickle
from WhoColor.parser import WikiMarkupParser
import cProfile
import pstats
import io

test_data = pickle.load(open('who_color_test_data.p','rb'))
#shrinked datasets - to check the validity quickly and fix the bugs
#test_data = pickle.load(open('who_color_test_data_shrinked.p','rb'))

pr = cProfile.Profile()
pr.enable()

print('Profiling the who color parser')
for article in test_data.keys():
    print(article)
    p = WikiMarkupParser(test_data[article]['rev_text'], test_data[article]['tokens'])
    #cProfile.run('p.generate_extended_wiki_markup()')
    #break
    p.generate_extended_wiki_markup()

pr.disable()

s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

# save the content into a file and 
