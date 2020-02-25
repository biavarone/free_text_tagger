# TexTa
TexTa is a tagger that extracts contextual information from free text.

Given a free text, the script is able to extract information about 4 categories: activities, emotions, interactions and places. For each of these categories there is a dictionary, which contains a list of sub-categories. 

Text given in input is parsed and then matched to the sub-categories by handwritten rules, which take into account syntactic information (lemmas, Parts-Of-Speech, dependency structure, ...).

## Requirements
- Requires Python 3.x
- Requires the following Python libraries:
	- [spaCy](https://spacy.io/) v2.2.3
	- [spaCy language model](https://spacy.io/usage/models) 'en_core_web_sm' v2.2.5
	- re
	
## Installing spaCy and needed models
- Install spaCy via pip or your preferred method (see [here](https://spacy.io/usage) for more details)

	`pip install -U spacy`

- Download language model

	`python spacy -m download en_core_web_sm`
	
## Input 
- text

[choose how to pass the text to the file and how to get the output]

## Output
For each category returns a `matches` list containing:

- a numeric id for the matched sub-category
- a number that states the point in the sentence where the match starts
- a number that states the point in the sentence where the match ends

e.g.
"_We're playing games_" will return this output:

- [(5133706519360878345, 2, 3), (5133706519360878345, 2, 4), (5133706519360878345, 3, 4)]

 - 5133706519360878345 is the id for the sub-category 'leisure'
 - 2,3 is the span for '_playing_'
 - 2,4 is the span for '_playing games_'
 - 3,4 is the span for '_games_'

 ! _notice that in the span interval, the first number is included, the second one is NOT included_
