# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

from spacy.matcher import Matcher
from utils import nlp

emotions_matcher = Matcher(nlp.vocab, validate=True)


# angry
angry1 = [{'LOWER': {'IN': ['aggressive', 'anger', 'angry', 'annoy', 'annoyed', 'annoying', 'betray', 'betrayed',
                            'bitter', 'critical', 'dismissive', 'disrespect', 'disrespected', 'disrespectful',
                            'distant', 'frustrate', 'frustrated', 'frustration', 'frustrating', 'furious', 'hostile',
                            'humiliate', 'humiliated', 'humiliating', 'indignant', 'infuriated', 'irritated',
                            'irritating', 'mad', 'numb', 'provoke', 'provoked', 'resentful', 'ridiculed', 'sceptic',
                            'sceptical', 'upset', 'violate', 'violated', 'withdraw', 'withdrawn']}}]
angry2 = [{'LEMMA': 'let', 'POS': 'VERB'}, {'LEMMA': 'down'}]
angry3 = [{'LEMMA': 'let', 'POS': 'VERB'}, {'LEMMA': 'me'}, {'LEMMA': 'down'}]

emotions_matcher.add('angry', None, angry1, angry2, angry3)


# bad
bad1 = [{'LOWER': {'IN': ['apathetic', 'bad', 'bored', 'boring', 'busy', 'drained', 'hopeless', 'indifferent', 'lost',
                          'overwhelmed', 'overwhelming', 'pressure', 'pressured', 'rush', 'rushed', 'sleepy', 'stress',
                          'stressed', 'tired', 'tiring', 'unfocused', 'worthless']}}]

emotions_matcher.add('bad', None, bad1)


# calm
calm1 = [{'LOWER': {'IN': ['calm', 'chilled', 'neutral', 'relaxed', 'rested', 'safe', 'secure']}}]
calm2 = [{'LEMMA': 'at'}, {'LEMMA': 'ease'}]

emotions_matcher.add('calm', None, calm1, calm2)


# disgusted
disgusted1 = [{'LOWER': {'IN': ['appalled', 'awful', 'detestable', 'disappointed', 'disappointing', 'disapproving',
                                'embarrassed', 'embarrassing', 'hesitant', 'horrified', 'judgmental', 'nauseated',
                                'nauseous', 'repelled', 'revolted']}}]

emotions_matcher.add('disgusted', None, disgusted1)

# fearful
fearful1 = [{'LOWER': {'IN': ['anxiety', 'anxious', 'concern', 'concerned', 'excluded', 'exposed', 'fearful',
                              'frightened', 'frightening', 'helpless', 'inadequate', 'inferior', 'insecure',
                              'insignificant', 'nervous', 'persecuted', 'rejected', 'scare', 'scaring', 'threatened',
                              'weak', 'worried', 'worry']}}]

emotions_matcher.add('fearful', None, fearful1)


# good
good1 = [{'LOWER': {'IN': ['alright', 'ok', 'okay']}}]
good2 = [{'LOWER': 'good', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('good', None, good1, good2)


# happy
happy1 = [{'LOWER': {'IN': ['accepted', 'amused', 'aroused', 'charmed', 'cheeky', 'confident', 'content', 'courageous',
                            'creative', 'curious', 'delighted', 'eager', 'empowered', 'energetic', 'enthusiastic',
                            'free', 'glad', 'grateful', 'happy', 'hopeful', 'inquisitive', 'inspired', 'interested',
                            'intimate', 'joyful', 'loving', 'optimistic', 'overjoyed', 'peaceful', 'proud', 'respected',
                            'sensitive', 'successful', 'thankful', 'trusting', 'valued']}}]

emotions_matcher.add('happy', None, happy1)


# sad
sad1 = [{'LOWER': {'IN': ['abandoned', 'ashamed', 'depression', 'depressed', 'despair', 'disappointed', 'disappointing',
                          'embarrassed', 'embarrassing', 'empty', 'fragile', 'grief', 'grieve', 'guilt', 'guilty',
                          'hurt', 'inferior', 'isolated', 'lonely', 'powerless', 'remorseful', 'sad', 'victimised',
                          'victimized', 'vulnerable']}}]

emotions_matcher.add('sad', None, sad1)


# surprised
surprised1 = [{'LOWER': {'IN': ['amazed', 'astonished', 'awe', 'confuse', 'confused', 'confusion', 'disillusioned',
                                'dismayed', 'excited', 'perplexed', 'shocked', 'startled', 'surprised']}}]

emotions_matcher.add('surprised', None, surprised1)
