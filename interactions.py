# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

from spacy.matcher import Matcher
from utils import nlp

interactions_matcher = Matcher(nlp.vocab, validate=True)


# alone
alone1 = [{'LEMMA': 'on'}, {'LOWER': 'my'}, {'LEMMA': 'own'}]
alone2 = [{'LEMMA': 'by'}, {'LOWER': 'myself'}]
alone3 = [{'LEMMA': 'alone', 'POS': {'IN': ['ADV', 'ADJ']}}]

interactions_matcher.add('alone', None, alone1, alone2, alone3)


# animal
animal1 = [{'LEMMA': {'IN': ['animal', 'cat', 'cub', 'dog', 'kitten', 'kitty', 'pet', 'pup', 'puppy']}, 'POS': 'NOUN'}]
animal2 = [{'LOWER': {'IN': ['doggie', 'doggo', 'doggy']}, 'POS': 'NOUN'}]

interactions_matcher.add('animal', None, animal1, animal2)


# cohabitants
cohabitants1 = [{'LEMMA': {'IN': ['cohabitant', 'flatmate', 'housemate', 'roommate']}, 'POS': 'NOUN'}]
cohabitants2 = [{'LOWER': {'IN': ['roomie', 'roomies', 'roomy']}, 'POS': 'NOUN'}]
cohabitants3 = [{'LEMMA': {'IN': ['flat', 'house', 'room']}, 'POS': 'NOUN'},
                {'IS_PUNCT': True, 'OP': '?'},
                {'LEMMA': 'mate', 'POS': 'NOUN'}]

interactions_matcher.add('cohabitants', None, cohabitants1, cohabitants2, cohabitants3)


# colleagues
colleagues1 = [{'LEMMA': {'IN': ['assistant', 'boss', 'chief', 'client', 'colleague', 'coworker', 'employee',
                                 'employer', 'fellow', 'workmate']}, 'POS': 'NOUN'}]
colleagues2 = [{'LEMMA': {'IN': ['co', 'fellow']}, 'POS': 'NOUN'},
               {'IS_PUNCT': True, 'OP': '?'},
               {'LEMMA': 'worker', 'POS': 'NOUN'}]
colleagues3 = [{'LEMMA': 'work', 'POS': 'NOUN'},
               {'IS_PUNCT': True, 'OP': '?'},
               {'LEMMA': 'mate', 'POS': 'NOUN'}]

interactions_matcher.add('colleagues', None, colleagues1, colleagues2, colleagues3)


# friends
friends1 = [{'LOWER': {'IN': ['bro', 'pal']}}]
friends2 = [{'LEMMA': {'IN': ['buddy', 'friend', 'mate']}, 'POS': 'NOUN'}]

interactions_matcher.add('friends', None, friends1, friends2)


# acquaintance
acquaintance1 = [{'LEMMA': {'IN': ['acquaintance', 'doctor', 'physician', 'professor', 'stranger',
                                   'teacher', 'vet', 'veterinary']}, 'POS': 'NOUN'}]
acquaintance2 = [{'LEMMA': 'g'}, {'IS_PUNCT': True}, {'LEMMA': 'p'}, {'IS_PUNCT': True}]  # g.p.
acquaintance3 = [{'LOWER': 'general'}, {'LOWER': 'practitioner'}]  # general practitioner
acquaintance4 = [{'LOWER': 'gp'}]  # gp

interactions_matcher.add('acquaintance', None, acquaintance1, acquaintance2, acquaintance3, acquaintance4)


# family
family1 = [{'LEMMA': {'IN': ['aunty', 'aunt', 'babe', 'baby', 'boy', 'brother', 'brotherinlaw', 'child', 'dad', 'dada',
                             'daddy', 'daughter', 'family', 'father', 'fatherinlaw', 'girl', 'grandad', 'granddad',
                             'grandchild', 'granddaughter', 'grandfather', 'grandma', 'grandmother', 'grandmam',
                             'grandmum', 'grandpa', 'grandson', 'granny', 'halfbrother', 'halfsister', 'infant', 'kid',
                             'kiddo', 'kiddos', 'ma', 'mama', 'mom', 'momma', 'mommy', 'mother', 'motherinlaw', 'mum',
                             'mummy', 'nana', 'nanny', 'nephew', 'niece' 'pa', 'pap', 'papa', 'pappa', 'parent', 'pop',
                             'poppa', 'relative', 'sib', 'sibling', 'sister', 'sisterinlaw', 'son', 'stepbrother',
                             'stepdad', 'stepdaddy', 'stepfather', 'stepmama', 'stepmom', 'stepmother', 'stepmum',
                             'stepparent' 'stepsister', 'toddler', 'unc', 'uncle']}, 'POS': 'NOUN'}]
family2 = [{'LEMMA': 'baby', 'POS': 'NOUN'}, {'LEMMA': {'IN': ['boy', 'girl']}, 'POS': 'NOUN'}]  # baby boy/girl
family3 = [{'POS': 'NOUN'},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': 'in'},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': 'law', 'POS': 'NOUN'}]  # so-in-law
family4 = [{'LEMMA': 'grand', 'POS': 'ADJ'},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': {'IN': ['child', 'dad', 'daughter', 'father', 'ma', 'mother', 'mam', 'mom', 'mum', 'pa', 'son',
                             'niece', 'newphew']}, 'POS': 'NOUN'}]  # grand-so
family5 = [{'LOWER': 'gramps'}]
family6 = [{'LEMMA': {'IN': ['half', 'step']}, 'POS': 'ADJ'},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': {'IN': ['brother', 'dad', 'daddy', 'father', 'mama', 'mom', 'mother', 'mum', 'parent', 'sister']},
            'POS': 'NOUN'}]  # half-sp
family7 = [{'LEMMA': 'in'}, {'IS_PUNCT': True}, {'LOWER': 'laws'}]  # in-laws
family8 = [{'LEMMA': 'twin'}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': 'NOUN', 'OP': '?'}]  # twin-brother/sister
family9 = [{'POS': 'NUM'},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': {'IN': ['month', 'year']}},
           {'IS_PUNCT': True, 'OP': '?'},
           {'LEMMA': 'old'}]  # 3-year/month-old

interactions_matcher.add('family', None, family1, family2, family3, family4, family5, family6, family7, family8,
                         family9,)


# partner
partner1 = [{'LEMMA': {'IN': ['boyfriend', 'bride', 'date', 'girlfriend', 'groom', 'husband', 'partner', 'spouse',
                              'wife']}, 'POS': 'NOUN'}]
partner2 = [{'LOWER': 'better'}, {'LEMMA': 'half', 'POS': 'NOUN'}]  # better half
partner3 = [{'LEMMA': 'significant'}, {'LEMMA': 'other'}]  # significant other
partner4 = [{'LOWER': {'IN': ['bae', 'fiance', 'fiancé', 'fiancee', 'fiancée']}}]
partner5 = [{'LEMMA': {'IN': ['bride', 'wife']}},
            {'IS_PUNCT': True, 'OP': '?'},
            {'LEMMA': 'to'},
            {'IS_PUNCT': True, 'OP': '?'},
            {'LEMMA': 'be'}]

interactions_matcher.add('partner', None, partner1, partner2, partner3, partner4, partner5)