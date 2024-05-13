# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:59:26 2023

@author: TomiComi
"""
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("hr_core_news_sm")
matcher = Matcher(nlp.vocab)

pattern = [{"LOWER": "tzv."}, {"LOWER": "primitivac"}]
matcher.add("primitivac_pattern", [pattern])

text = "Ovaj tzv. primitivac ne zna ništa o tehnologiji."
doc = nlp(text)

matches = matcher(doc)
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
