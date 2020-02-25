# -*- coding: utf-8  -*-
# !/usr/bin/python3

__author__ = "biavarone"

from spacy.matcher import Matcher
from utils import nlp

activities_matcher = Matcher(nlp.vocab, validate=True)


# doing-chores
chores1 = [{'POS': 'VERB', 'OP': '?'},
           {'POS': 'DET', 'OP': '?'},
           {'LEMMA': {'IN': ['chore', 'laundry']}, 'POS': 'NOUN'}]
chores2 = [{'LEMMA': {'IN': ['clean', 'iron', 'hoover', 'vacuum']}, 'POS': 'VERB'},
           {'POS': 'DET', 'OP': '?'},
           {'POS': 'NOUN', 'OP': '?'}]

activities_matcher.add('chores', None, chores1, chores2)


# communicating
communicating1 = [{'LEMMA': {'IN': ['chat', 'communicate', 'converse', 'socialise', 'socialize', 'speak', 'talk']},
                   'POS': 'VERB'}]

activities_matcher.add('communicating', None, communicating1)


# commuting
commuting1 = [{'LEMMA': {'IN': ['aeroplane', 'airplane', 'bus', 'cab', 'car', 'chopper', 'metro', 'motorbike',
                                'motorcycle', 'moped', 'plane', 'taxi', 'train', 'tram', 'tube', 'underground']},
               'POS': 'NOUN'}]
commuting2 = [{'LOWER': 'motor'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'scooter'}]
commuting3 = [{'LEMMA': {'IN': ['commute', 'drive', 'travel']}, 'POS': {'IN': ['NOUN', 'VERB']}}]
commuting4 = [{'LEMMA': {'NOT_IN': ['gas']}, 'POS': 'NOUN', 'OP': '?'}, {'LOWER': 'station', 'POS': 'NOUN'}]  # compounds with station

activities_matcher.add('commuting', None, commuting1, commuting2, commuting3, commuting4)


# cooking-food
cook1 = [{'LEMMA': {'IN': ['bake', 'cook', 'prepare']}, 'POS': 'VERB'}, {'POS': 'DET', 'OP': '?'},
         {'POS': {'IN': ['NOUN', 'PRON']},  'OP': '?'}]  # bake a cake, cook a meal
cook2 = [{'LOWER': 'foodprep'}]
cook3 = [{'LOWER': 'food'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': {'IN': ['prep', 'preparation']}}]

activities_matcher.add('cooking', None, cook1, cook2, cook3)


# drinking-alcohol
alcohol1 = [{'POS': 'VERB', 'OP': '?'},
            {'POS': 'DET', 'OP': '?'},
            {'LEMMA': {'IN': ['can', 'glass', 'pint']}, 'POS': {'NOT_IN': ['VERB', 'AUX']}, 'OP': '?'},
            {'LEMMA': 'of', 'OP': '?'},
            {'LEMMA': {'IN': ['ale', 'beer', 'bread', 'cider', 'cocktail', 'liquor', 'mead', 'pint', 'wine']},
             'POS': 'NOUN'}]

alcohol2 = [{'POS': 'VERB', 'OP': '?'},
            {'POS': 'DET', 'OP': '?'},
            {'LEMMA': 'drink', 'POS': {'NOT_IN': ['VERB']}}]

activities_matcher.add('alcohol', None, alcohol1, alcohol2)


# eating
eating1 = [{'LEMMA': 'eat', 'POS': 'VERB'}]  # verbs
eating2 = [{'LEMMA': 'ice'}, {'LEMMA': 'cream'}]  # compound
eating3 = [{'LEMMA': 'fast'}, {'LEMMA': 'food'}]  # compound
eating4 = [{'LEMMA': {'NOT_IN': ['cook', 'prepare', 'make']}},
           {'POS': 'DET', 'OP': '?'},
           {'LEMMA': {'IN': ['almond', 'americano', 'apple', 'avocado', 'banana', 'beef', 'breakfast', 'brunch',
                             'burger', 'burrito', 'cake', 'carrot', 'cheese', 'chip', 'chocolate', 'coffee', 'cookie',
                             'corn', 'cracker', 'crisp', 'dinner', 'doughnut', 'egg', 'espresso', 'food', 'fry',
                             'grape', 'juice', 'lunch', 'macchiato', 'milk', 'milkshake', 'nut', 'oat', 'oatmeal', 'pasta',
                             'peanut', 'pizza', 'potato', 'raisin', 'sandwich', 'smoothie', 'snack', 'soda',
                             'spaghetti', 'sushi', 'taco', 'tea', 'tuna', 'water', '7up', 'cola', 'pepsi', 'sprite']},
            'POS': {'IN': ['NOUN', 'PROPN']}}]  # eat my meal/some food
eating5 = [{'LEMMA': {'IN': ['almond', 'americano', 'apple', 'avocado', 'banana', 'beef', 'breakfast', 'brunch',
                             'burger', 'burrito', 'cake', 'carrot', 'cheese', 'chip', 'chocolate', 'coffee', 'cookie',
                             'corn', 'cracker', 'crisp', 'dinner', 'doughnut', 'egg', 'espresso', 'food', 'fry',
                             'grape', 'juice', 'lunch', 'macchiato', 'milk', 'milkshake', 'nut', 'oat', 'oatmeal', 'pasta',
                             'peanut', 'pizza', 'potato', 'raisin', 'sandwich', 'smoothie', 'snack', 'soda',
                             'spaghetti', 'sushi', 'taco', 'tea', 'tuna', 'water', '7up', 'cola', 'pepsi', 'sprite']},
            'POS': {'IN': ['NOUN', 'PROPN']}}]  # eat my meal/some food

activities_matcher.add('eating', None, eating1, eating2, eating3, eating4, eating5)


# grooming
grooming1 = [{'LEMMA': 'groom', 'POS': 'VERB'}]
grooming2 = [{'LEMMA': 'hair'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'cut'}]  # hair-cut
grooming3 = [{'LEMMA': 'brush', 'POS': 'VERB'}, {'POS': 'DET'},
             {'LEMMA': {'IN': ['hair', 'tooth']}}]  # brush my hair/teeth
grooming4 = [{'POS': 'VERB', 'OP': '?'},
             {'POS': 'DET', 'OP': '?'},
             {'LEMMA': {'IN': ['bath', 'shave', 'shower', 'haircut']}}]  # taking/having a bath

activities_matcher.add('grooming', None, grooming1, grooming2, grooming3, grooming4)


# leisure
leisure1 = [{'POS': 'VERB', 'OP': '?'},
            {'POS': 'ADP', 'OP': '?'},
            {'POS': 'DET', 'OP': '?'},
            {'LEMMA': {'IN': ['article', 'banjo', 'bass', 'book', 'cello', 'clarinet', 'comic', 'computer', 'cornamuse',
                              'dance', 'drum', 'film', 'flute', 'game', 'guitar', 'harp', 'horn', 'laptop', 'leisure',
                              'movie', 'music', 'novel', 'newspaper', 'ocarina', 'oboe', 'online', 'pc', 'phone',
                              'play', 'piano', 'piece', 'radio', 'saxophone', 'serie', 'show', 'song', 'telephone',
                              'television', 'trombone', 'trumpet', 'tuba', 'tv', 'video', 'videogame', 'violin']},
             'POS': 'NOUN'},
            {'IS_PUNCT': True, 'OP': '?'},
            {'POS': 'NOUN', 'OP': '?'}]  # nouns
leisure2 = [{'LEMMA': {'IN': ['camp', 'dance', 'draw', 'game', 'knit', 'paint', 'play', 'read', 'sculpt', 'shop', 'sing']},
             'POS': 'VERB'}]  # verbs
leisure3 = [{'LOWER': {'IN': ['gardening']}, 'POS': 'NOUN'}]  # lower
leisure4 = [{'POS': 'VERB', 'OP': '?'},
            {'POS': 'DET', 'OP': '?'},
            {'POS': 'NOUN', 'OP': '?'},
            {'POS': 'ADP', 'OP': '?'},
            {'LOWER': {'IN': ['netflix', 'prime', 'series', 'youtube']}, 'POS': 'PROPN'}]
leisure5 = [{'LOWER': 'on'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'line'}]  # on-line
leisure6 = [{'LOWER': 't'}, {'IS_PUNCT': True}, {'LOWER': 'v'}, {'IS_PUNCT': True}]  # t.v.
leisure7 = [{'LOWER': 'you'}, {'LOWER': 'tube'}]  # you tube
leisure8 = [{'LEMMA': 'do', 'POS': {'IN': ['AUX', 'VERB']}}, {'LEMMA': 'craft', 'POS': 'NOUN'}]  # do craft

activities_matcher.add('leisure', None, leisure1, leisure2, leisure3, leisure4, leisure5, leisure6, leisure7, leisure8)


# relaxing
relaxing1 = [{'LEMMA': {'IN': ['chill', 'relax']}, 'POS': 'VERB'}]
relaxing2 = [{'LEMMA': {'IN': ['chilling', 'relaxing']}, 'POS': 'NOUN'}]
activities_matcher.add('relaxing', None, relaxing1, relaxing2)


# sleeping
sleeping1 = [{'LEMMA': {'IN': ['nap', 'sleep']}, 'POS': {'IN': ['NOUN', 'VERB']}}]

activities_matcher.add('sleeping', None, sleeping1)


# smoking
smoking1 = [{'POS': 'VERB', 'OP': '?'},
            {'POS': 'DET', 'OP': '?'},
            {'LEMMA': {'IN': ['cigar', 'cigarette', 'joint', 'skunk', 'tobacco', 'weed']}, 'POS': 'NOUN'}]
smoking2 = [{'LEMMA': 'smoke', 'POS': 'VERB'}]
smoking3 = [{'LEMMA': 'smoking', 'POS': 'NOUN'}]

activities_matcher.add('smoking', None, smoking1, smoking2, smoking3)


# sport
sport1 = [{'POS': 'VERB', 'OP': '?'},
          {'POS': 'DET', 'OP': '?'},
          {'LOWER': {'IN': ['athletics', 'gymnastics', 'marathon', 'pentathlon', 'tetrathlon', 'triathlon']},
           'POS': {'IN': ['NOUN', 'PROPN']}}]
sport2 = [{'POS': 'VERB', 'OP': '?'},
          {'LOWER': {'IN': ['baseball', 'basket', 'basketball', 'bike', 'biking', 'bicycle', 'boulder', 'bouldering',
                            'canoe', 'canoeing', 'climb', 'climbing', 'cycle', 'cycling', 'dive', 'diving', 'exercise',
                            'exercising', 'exercize', 'exercizing', 'football', 'golf', 'hike', 'hiking', 'hockey',
                            'hokey', 'kayak', 'kayaking', 'polo', 'punt', 'punting', 'row', 'rowing', 'run', 'running',
                            'sail', 'sailing', 'skate', 'skating', 'ski', 'skiing', 'skydive', 'skydiving', 'soccer',
                            'squash', 'swim', 'swimming', 'tennis', 'trek', 'trekking', 'volley', 'volleyball', 'walk',
                            'walking', 'weightlift', 'weightlifting']}, 'POS': 'NOUN'}]
sport3 = [{'LEMMA': {'IN': ['bike', 'bicycle', 'boulder', 'canoe', 'climb', 'cycle', 'dive', 'exercise', 'exercize',
                            'golf', 'hike', 'kayak', 'punt', 'row', 'rowing', 'run', 'sail', 'skate', 'ski', 'skydive',
                            'swim', 'trek', 'walk', 'weightlift']}, 'POS': 'VERB'}]

sport4 = [{'LOWER': 'scuba'}, {'LOWER': 'diving'}]
sport5 = [{'LOWER': 'scuba'}, {'IS_PUNCT': True}, {'LOWER': 'diving'}]
sport6 = [{'LEMMA': 'weight'}, {'IS_PUNCT': True}, {'LEMMA': {'IN': ['lift', 'lifting']}}]

activities_matcher.add('sport', None, sport1, sport2, sport3, sport4, sport5, sport6)


# work-study
work_study1 = [{'LEMMA': {'IN': ['essay', 'exam', 'homework', 'revision']}, 'POS': 'NOUN'}]
work_study2 = [{'LEMMA': {'IN': ['learn', 'revise', 'study', 'work']}, 'POS': 'VERB'}]

activities_matcher.add('workstudy', None, work_study1, work_study2)
