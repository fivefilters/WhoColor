import sys

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    print(path.dirname(path.dirname(path.abspath(__file__))))
	
	
from WhoColor.utils import WikipediaRevText, WikiWhoRevContent
from WhoColor.parser import WikiMarkupParser

class WhoColorParser(object):

    def __init__(self, page_title=None, page_id=None, rev_id=None):
        self.page_id = page_id
        self.page_title = page_title
        self.rev_id = rev_id

    def handle(self):
        wp_rev_text_obj = WikipediaRevText(page_title=self.page_title)
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

        html = wp_rev_text_obj.convert_wiki_text_to_html(p.extended_wiki_text)
        return html

        # to convert (extended) wiki text into html by using wp api
        # rev_extended_html = wp_rev_text_obj.convert_wiki_text_to_html(wiki_text=rev_data['rev_text'])

article = 'German_federal_election,_2017'
#article = 'Honors_at_Dawn'
whoObject = WhoColorParser(article)
html = whoObject.handle()
print(html)