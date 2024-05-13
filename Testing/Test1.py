# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:38:28 2023

@author: TomiComi
"""
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("hr_core_news_lg")
matcher = Matcher(nlp.vocab)
# Add match ID "HelloWorld" with no callback and one pattern
pattern = [{"TEXT":{"REGEX":  'tzv\.\s*(primitivac)'}}]
matcher.add("HelloWorld", [pattern])

f = open("1960.txt", 'r',encoding="utf8")
content = f.read()
#print(content)
f.close()


doc=nlp(content)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)