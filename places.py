# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

from spacy.matcher import Matcher
from utils import nlp

places_matcher = Matcher(nlp.vocab, validate=True)

# education
education1 = [{'LEMMA': {'IN': ['campus', 'class', 'classroom', 'college', 'school', 'university']}, 'POS': 'NOUN'}]
education2 = [{'LEMMA': 'uni', 'POS': {'IN': ['NOUN', 'PROPN']}}]

places_matcher.add('education', None, education1, education2)


# home
home1 = [{'LEMMA': {'IN': ['bathroom', 'bed', 'bedroom', 'couch', 'garage', 'home', 'kitchen', 'pantry', 'restroom',
                           'sofa']}, 'POS': 'NOUN'}]
home2 = [{'POS': 'NOUN'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'room', 'POS': 'NOUN'}]  # st-room


places_matcher.add('home', None, home1, home2)


# hospital
hospital1 = [{'LEMMA': {'IN': ['hospital']}, 'POS': 'NOUN'}]

places_matcher.add('hospital', None, hospital1)


# hotel
hotel1 = [{'LEMMA': {'IN': ['hotel', 'motel']}, 'POS': 'NOUN'}]
hotel2 = [{'LOWER': {'IN': ['airbnb', 'bnb']}, 'POS': 'NOUN'}]

places_matcher.add('hotel', None, hotel1, hotel2)


# leisure
leisure1 = [{'LEMMA': {'IN': ['bookstore', 'bookshop', 'cafe', 'café', 'cafè', 'cinema', 'club', 'gym', 'gymnasium',
                              'library', 'museum', 'pool', 'pub', 'restaurant', 'shop', 'store', 'theater', 'theatre']},
             'POS': 'NOUN'}]
leisure2 = [{'LEMMA': 'coffee', 'POS': 'NOUN'}, {'LEMMA': 'place', 'POS': 'NOUN'}]
leisure3 = [{'LEMMA': {'IN': ['gym', 'gymnasium']}, 'POS': 'NOUN'}]
leisure4 = [{'LEMMA': 'swimming', 'POS': 'NOUN'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'pool', 'POS': 'NOUN'}]
leisure5 = [{'POS': 'NOUN'},
            {'IS_PUNCT': True, 'OP': '?'},
            {'LEMMA': {'IN': ['theater', 'theatre']}, 'POS': 'NOUN'}]

places_matcher.add('leisure', None, leisure1, leisure2, leisure3, leisure4, leisure5)


# outdoor
outdoor1 = [{'LEMMA': {'IN': ['backyard', 'beach', 'camp', 'cliff', 'forest', 'garden', 'hill', 'hillside', 'hilltop',
                              'lake', 'mountain', 'mountainside', 'park', 'ath', 'peak', 'river', 'sea', 'seashore',
                              'seaside', 'shore', 'trail', 'wood', 'yard']}, 'POS': 'NOUN'}]
outdoor2 = [{'LEMMA': {'IN': ['back', 'front']}},
            {'IS_PUNCT': True},
            {'LEMMA': {'IN': ['garden', 'yard']}, 'POS': 'NOUN'}]
outdoor3 = [{'LEMMA': {'IN': ['hill', 'mountain', 'sea']}, 'POS': 'NOUN'},
            {'IS_PUNCT': True, 'OP': '?'},
            {'LEMMA': {'IN': ['shore', 'side', 'top']}, 'POS': 'NOUN'}]

outdoor4 = [{'LEMMA': 'outdoor', 'POS': {'IN': ['ADJ', 'ADV']}}]
outdoor5 = [{'LEMMA': 'outside', 'POS': 'ADV'}]
outdoor6 = [{'LEMMA': 'sport', 'POS': 'NOUN'}, {'LEMMA': 'ground', 'POS': 'NOUN'}]

places_matcher.add('outdoor', None, outdoor1, outdoor2, outdoor3, outdoor4, outdoor5, outdoor6)


# workplace
workplace1 = [{'LEMMA': {'IN': ['administration', 'job', 'office', 'work', 'workplace']}, 'POS': 'NOUN'}]
workplace2 = [{'LEMMA': 'work', 'POS': 'NOUN'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'place', 'POS': 'NOUN'}]

places_matcher.add('workplace', None, workplace1, workplace2)




