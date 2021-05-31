import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w= w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: 
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0 :
        message = input("Did you mean %s instead? Enter Yes or No (Y/N) :" % get_close_matches(w,data.keys())[0])
        message=message.upper()
        if message[0]=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist."

word=input("Enter the word you want to search: ")


output = translate(word)
i=1
if type(output) == list:
    for a in output :
        print(" ",i,".",a)
        i=i+1
else:
    print(output)

