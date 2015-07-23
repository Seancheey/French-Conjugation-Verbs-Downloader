# -*- coding: UTF-8-* -*-
__author__ = 'Seancheey'

import urllib
import urllib2
import re


def getResponse(verb):
    try:
        return urllib.urlopen('http://www.conjugation-fr.com/conjugate.php' + '?verb=' + verb + '&x=0&y=0')
    except urllib2.HTTPError, e:
        if hasattr(e, 'reason'):
            print e.reason
        if hasattr(e, 'code'):
            print e.code
    except urllib2.URLError, u:
        print u.reason

def deleteTags(string):
    pattern = re.compile(r'\<(\s|\S)*?(?<=\>)')
    return re.sub(pattern, '', string)


person = [r'(je |j\')', r'tu ', r'il ', r'nous ', r'vous ', r'ils ']
verbs = ['etre', 'avoir', 'regarder', 'faire', 'aller', 'attendre', 'pouvoir', 'vouloir', 'devoir', 'preferer', 'laver',
         'dormir', 'partir', 'courir']
text = ''

for v in verbs:
    message = getResponse(v).read()
    message = deleteTags(message)
    text += '\n---' + v + '---:\n'
    print 'fetching '+v+'...'
    for p in person:
        pattern = re.compile(p + '.*', flags=re.I)
        match = re.search(pattern, message)
        if match:
            text += match.group()
        else:
            text += 'not match'
        text += '\n'

f = open('french conjugation', 'w')
text = re.sub(r' ','\t',text)
text = re.sub(r'\'','\t\'',text)
f.write(text)
f.close()
print text
print '-------EOF------'