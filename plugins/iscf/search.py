import os
import pandas as pd
import html

INDEX_CSV = os.getenv('INDEX_FILE')

def se(args):
    index = pd.read_csv(INDEX_CSV)
    q = args.split(" ")

    res = ''
    for idx, r in index.iterrows():
        if any([True for qi in q if r[0].lower().find(qi.lower()) > -1]):
            res += '- <' + r['Link'] + '|' + r['Name'] + '>\n'
    if len(res) == 0:
        return html.escape('Ooops! Can\'t find what you are looking for.')
    return html.escape('**I found something for you:**\n\n\n' + res)

if '__main__' == __name__:
    print(se('abc swot'))