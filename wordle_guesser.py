"""
Wordle guesser script
"""

import re
import string

from nltk.corpus import words
fivelwords = [word for word in words.words() if len(word) == 5]

# introduction
print("Welcome to the Wordle guesser script. You will be asked for 3 inputs:\n\n* For letters at known positions, type any letters whose position is known, and underscores where the letter is not known (e.g. 'f_b__').\n\n* For letters present elsewhere in the word: for each position enter one or more letters not present here, or an underscore if none, separated by commas (e.g. l,_,_,ae,_).\n\n* For letters not present in the word, enter all the letters as one string (e.g. 'imps'), or leave blank if none.")

# get the known letters
while True:
    known_letters = input("Enter letters at known positions: " )
    if (len(known_letters) != 5) or not (known_letters.replace("_", "").isalpha() or known_letters == "_____"):
        print("Input must be 5 characters long and consist of only letters and underscores.")
        continue
    else:
        break

# get potential letters at each position
known_letters = list(known_letters)
for i in range(0,5):
    if known_letters[i] == "_":
        known_letters[i] = string.ascii_lowercase
        
# get letters that are present but not in certain positions
while True:
    other_letters = input("Enter letters present elsewhere in the word: ")
    if (other_letters.count(",") != 4) or not (re.sub("_|,","",other_letters).isalpha() or re.sub("_|,","",other_letters) == ""):
        print("Input must be five strings of letters or underscores, separated by commas.")
        continue
    else:
        break
        
other_letters = other_letters.lower()
letters_in = other_letters
other_letters = other_letters.split(",")
for i in range(len(other_letters)):
    other_letters[i] = other_letters[i].replace("_","")

letters_in = re.sub("_|,","",letters_in)
letters_in = set(letters_in)

# get letters not in the word
while True:
    letters_out = input("Enter letters NOT in the word: ")
    if not letters_out.isalpha() and letters_out != "":
        print("Input must be either a string of letters or blank.")
        continue
    else:
        break
letters_out = set(letters_out)

# filter for words with the known letters at these positions
filtered_known = [word for word in fivelwords
          if (word[0] in known_letters[0] and
              word[1] in known_letters[1] and
              word[2] in known_letters[2] and
              word[3] in known_letters[3] and
              word[4] in known_letters[4] and
              all(x in word for x in letters_in) and
              all(y not in word for y in letters_out))]
          
# filter to words without the "other" letters at those positions
filtered_all = [word for word in filtered_known
             if(word[0] not in other_letters[0] and
                word[1] not in other_letters[1] and
                word[2] not in other_letters[2] and
                word[3] not in other_letters[3] and
                word[4] not in other_letters[4])]
print("\nSuggested words: ")
print(*set(filtered_all), sep=", ") 
