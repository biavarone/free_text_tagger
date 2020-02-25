# -*- coding: utf-8  -*-

__author__ = "biavarone"

from utils import *
from activities import activities_matcher
from emotions import emotions_matcher
from interactions import interactions_matcher
from places import places_matcher


def match_places(sentence):
    found = places_matcher(sentence)
    all_matches = []

    for match_id, start, end in found:
        if check_negation(sentence[start]):
            pass
        else:
            all_matches.append((match_id, start, end))

    return all_matches


def match_interactions(sentence):
    found = interactions_matcher(sentence)
    all_matches = []  # TODO longest match

    for match_id, start, end in found:
        if check_negation(sentence[start]):
            pass
        else:
            all_matches.append((match_id, start, end))

    return all_matches


def match_emotions(sentence):
    found = emotions_matcher(sentence)
    all_matches = []

    for match_id, start, end in found:
        if check_negation(sentence[start]):
            pass
        else:
            all_matches.append((match_id, start, end))

    return all_matches


def match_activities(sentence):
    found = activities_matcher(sentence)  # all matches, to be checked for negation
    all_matches = []  # all matches # TODO find longest match if needed

    for match_id, start, end in found:
        if check_negation(sentence[start]):
            pass
        else:
            all_matches.append((match_id, start, end))

    return all_matches


if __name__ == "__main__":

    sentence = "Sentence to be analyzed"

    # analyze sentence
    sentence = substitute_dash(sentence)  # substitute dash with full stop for better parsing
    sentence = nlp(sentence)

    for sent in sentence.sents:
        sent = sent.as_doc()

        activities_tags = match_activities(sent)
        if activities_tags:
            # match_id is a number associated to the matched category, i.e. 5133706519360878345 == 'leisure'
            for match_id, start, end in activities_tags:
                rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'leisure'
                span = sent[start: end]  # get the matched slice of the sentence
                print("activities: {rule_id}: {span}")

        emotions_tags = match_emotions(sent)
        if emotions_tags:
            # match_id is a number associated to the matched category, i.e. 9391526999249888540 == 'sad'
            for match_id, start, end in emotions_tags:
                rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'sad'
                span = sent[start: end]  # get the matched slice of the sentence
                print(f"emotions: {rule_id}: {span}")
        
        interactions_tags = match_interactions(sent)
        if interactions_tags:
            for match_id, start, end in interactions_tags:
                # match_id is a number associated to the matched category, i.e. 18292453351080475948 == 'family'
                rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'family'
                span = sent[start: end]  # get the matched slice of the sentence
                print("interactions: {rule_id}: {span}")
        
        places_tags = match_places(sent)
        if places_tags:
            for match_id, start, end in places_tags:
                # match_id is a number associated to the matched category, i.e. 12006852138382633966 == 'home'
                rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'home'
                span = sent[start: end]  # get the matched slice of the sentence
                print("places: {rule_id}: {span}")

    
