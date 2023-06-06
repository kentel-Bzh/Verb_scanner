import json

text = str(input("enter text: "))

#convert json verb list to dict.
with open("verbes.json") as verbs:
    conjugaisons = json.load(verbs)
    
#convert input text to list
text_list = text.split(" ")
print(text_list)

for word in text_list:
    for key, value in conjugaisons.items():
        if word == conjugaisons[value]:
            print(word)
    else:
        print("pas de verbe listé")
