# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

import re
import spacy

nlp = spacy.load('en_core_web_sm')


def is_adjective(token):
    if token.pos_ == 'ADJ':
        return True
    else:
        return False


def is_noun(token):
    if token.pos_ == 'NOUN':
        return True
    else:
        return False


def is_verb(token):
    if token.pos_ == 'VERB':
        return True
    else:
        return False


def is_auxiliary_verb(token):
    if token.pos_ == 'AUX':
        return True
    else:
        return False


def is_pronoun(token):
    if token.pos_ == 'PRON':
        return True
    else:
        return False


def find_verbal_head(token):
    if token.head.pos_ == 'VERB' or token.head.pos_ == 'AUX':
        # gives back the position of the verb in the sentence
        return token.head
    else:
        if token.head != token.head.head:
            return find_verbal_head(token.head)
        else:
            return None


def check_negation(token):
    negatives = ['nothing', 'nobody', 'no']
    # TODO collapse repeated things if possible

    # NEGATION WITH ADJECTIVES
    if is_adjective(token):
        # nothing to be/feel upset about
        if is_verb(token.head) or is_auxiliary_verb(token.head):
            if is_pronoun(token.head.head) and token.head.head.lemma_ in negatives:
                return True
        # I am not busy
        for child in token.head.children:
            if child.dep_ == 'neg':
                return True
        # Not too bad
        for child in token.children:
            if child.dep_ == 'neg':
                return True
        # Not that happy
        if token.head.pos_ == 'amod' or token.head.pos_ == 'advmod':
            if token.head.head and token.head.head.pos_ == 'neg':
                return True

    # NEGATION WITH VERBS
    if is_verb(token):
        # I have nothing stressing me
        if is_pronoun(token.head) and token.head.lemma_ in negatives:
            return True
        # I have nobody stressing me
        for child in token.children:
            if is_pronoun(child) and child.lemma_ in negatives:
                return True
        # I have no one stressing me
        if is_noun(token.head):
            for child in token.head.children:
                if child.lemma_ in negatives:
                    return True
        # I'm not working
        for child in token.children:
            if child.dep_ == 'neg':
                return True

    # NEGATION WITH NOUNS
    if is_noun(token):
        # find the head of the noun
        verb = find_verbal_head(token)
        if verb:
            for child in verb.children:
                if child.dep_ == 'neg':
                    return True
        # expression like "no stress"
        for child in token.children:
            if child.lemma_ == 'no':
                return True
        # ?
        if token.head.pos_ == 'amod' or token.head.pos_ == 'advmod':
            if token.head.head and token.head.head.pos_ == 'neg':
                return True


def substitute_dash(sentence):
    sentence = re.sub(r' - ', '. ', sentence)
    return sentence
