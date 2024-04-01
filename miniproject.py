import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = get_close_matches(word, data.keys())[0]
        response = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ")
        if response.lower() == 'y':
            return data[suggestion]
        else:
            return "The word doesn't exist. Please double check it."
    else:
        return "The word doesn't exist. Please double check it."

word_input = input("Enter a word: ")
output = get_definition(word_input)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)