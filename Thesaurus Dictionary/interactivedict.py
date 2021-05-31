import mysql.connector
import json
import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database = "ardit700_pm1database"
)



word = input("Enter the word: ")

cursor = con.cursor()

query=cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results=cursor.fetchall()

def translate(w):
    w= w.lower()
    if w in results:
        return results[w]
    elif w.title() in results: 
        return results[w.title()]
    elif w.upper() in results:
        return results[w.upper()]
    elif len(get_close_matches(w,results.keys()))>0 :
        message = input("Did you mean %s instead? Enter Yes or No (Y/N) :" % get_close_matches(w,results.keys())[0])
        message=message.upper()
        if message[0]=='Y':
            return results[get_close_matches(w,results.keys())[0]]
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist."

if type(results)==list:
    for res in results:
        print(translate(res[1]))
else:
    print("No words found")