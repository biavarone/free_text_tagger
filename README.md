# TexTa
TexTa is a tagger that extracts contextual information from free text.

Given a free text, the script is able to extract information about 4 categories: activities, emotions, interactions and places. For each of these categories there is a dictionary, which contains a list of sub-categories. 

Text given in input is parsed and then matched to the sub-categories by handwritten rules, which take into account syntactic information (lemmas, Parts-Of-Speech, dependency structure, ...).

## Requirements
- Requires Python 3.x
- Requires the following Python libraries:
	- [spacy](https://spacy.io/) 
	- re

## Input
- Text (string)

-- choose how to pass string to the main script --


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
