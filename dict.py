import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def find_meaning(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        word = get_close_matches(word, data.keys())[0]
        y = input("Word not found.Do you mean '" + word + "' (y/n):")
        if 'y' == y.lower():
            return data[str(word)]
        else:
            return 'No match found'
    else:
        return "no word found!!  Please try checking spelling "


choice = 'y'
while choice =='y':
    word = input("Enter word : ")
    output = find_meaning(word)
    if type(output)==list:
        for item in output:
            print('* '+item)
    else:
        print('* '+output)
    choice = input("\nWant to search more (Y/N): ").lower()
print("Thank YOU!! good bye ")