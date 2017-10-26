import sys
#sys.path.append('H:\wiki-who\WhoColor\WhoColor')

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    print(path.dirname(path.dirname(path.abspath(__file__))))

from WhoColor.utils import WikipediaRevText
from WhoColor.utils import WikiWhoRevContent
from WhoColor.parser import WikiMarkupParser

import pickle

test_articles = ['Amstrad CPC', 'Antarctica', 'Apollo 11', 'Armenian Genocide', 'Barack_Obama',
                 'Bioglass', 'Bothrops_jararaca', 'Chlorine', 'Circumcision', 'Communist Party of China',
                 'Democritus', 'Diana,_Princess_of_Wales', 'Encryption', 'Eritrean Defence Forces',
                 'European Free Trade Association', 'Evolution', 'Geography of El Salvador', 'Germany',
                 'Home and Away', 'Homeopathy', 'Iraq War', 'Islamophobia', 'Jack the Ripper', 'Jesus',
                 'KLM destinations', 'Lemur', 'Macedonians_(ethnic_group)', 'Muhammad', 'Newberg, Oregon',
                 'Race_and_intelligence', 'Rhapsody_on_a_Theme_of_Paganini', 'Robert Hues', "Saturn's_moons_in_fiction",
                 'Sergei Korolev', 'South_Western_main_line', 'Special Air Service', 'The_Holocaust', 'Toshitsugu_Takamatsu',
                 'Vladimir_Putin', 'Wernher_von_Braun']

test_data ={}
try:
    test_data = pickle.load(open('who_color_test_data.p', 'rb'))
except:
    test_data ={}

for test_article in test_articles:
    print(test_article,' started ...')
    if test_article not in test_data.keys():
        wp_rev_text_obj = WikipediaRevText(page_title=test_article)
        # to get rev wiki text from wp api
        # page_id, namespace, rev_id, rev_text
        rev_data = wp_rev_text_obj.get_rev_wiki_text()

        ww_rev_content = WikiWhoRevContent(page_id=rev_data['page_id'])
        # revisions {rev_id: [timestamp, parent_id, class_name/editor, editor_name]}
        # tokens [[conflict_score, str, o_rev_id, in, out, editor/class_name, age]]
        # biggest conflict score (int)
        wikiwho_data = ww_rev_content.get_revisions_and_tokens()

        p = WikiMarkupParser(rev_data['rev_text'], wikiwho_data['tokens'])
        p.generate_extended_wiki_markup()

        test_data[test_article] = {'rev_text': rev_data['rev_text'], 'tokens': wikiwho_data['tokens'],
                                   'extended_wiki_markup':p.extended_wiki_text,
                                   'present_editors':p.present_editors}
        pickle.dump(test_data, open('who_color_test_data.p', 'wb'))
    print(test_article, ' ended ...')

#compare_test_data = pickle.load(open('who_color_test_data.p', 'rb'))

#print(id(test_data))
#print(id(compare_test_data))
#print(test_data == compare_test_data)

# compare_test_data['extra'] = 'something that i want to add'
# print(test_data == compare_test_data)
print('End of program')