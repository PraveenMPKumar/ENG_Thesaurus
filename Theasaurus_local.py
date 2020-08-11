import json
from difflib import get_close_matches

#Storing data from json file
data = json.load(open("data.json"))
closest_words = []

#Function to fetch the meaning
def get_meaning(word):
    w = word.lower()
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]

    elif if_close_match_exists(w):
        yn = input(
            "Did you mean %s instead ?, If Yes enter y, else No enter n : " % closest_words[0])

        if yn == "y" or yn == "Y":
            return get_meaning(closest_words[0])
        elif yn == "n" or yn == "N":
            return "The word doesn't exist, Please double check !"
        else:
            return "Invalid input, Please Try Again !"
    else:
        return "Word doesn't exists. Please double check !"

#Function to check close match if typo from user
def if_close_match_exists(w):
    closest_words.extend(get_close_matches(w, data.keys(), 5, 0.8))
    return len(closest_words) > 0

#Program run code
while True:
    user_input = input("Enter a word :")
    closest_words.clear()
    output = get_meaning(user_input)
    if type(output) == list:
        for word in output:
            print(word)
    else:
        print(output)
    to_continue = input("Press q to quit:")

    if to_continue == "q" or to_continue == "Q":
        break