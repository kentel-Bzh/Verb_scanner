import json

text = str(input("enter text: "))

#convert json verb list to dict.
conjugaisons = []
with open("verbes.json") as verbs:
    conjugaisons = json.load(verbs)
    
#convert input text to list
text_list = text.split(" ")
print(text_list)

found = False
for word in text_list:    
    for verb in conjugaisons:
        # Need to add search for other keys, not just indicatif present
        if 'indicatif' in verb:
            indic = verb['indicatif']['prĂ©sent']
            if word in indic:
                print("Found verb:")
                print(verb)
                found |= True
                break
            
if found == False:
    print("pas de verbe listé")
