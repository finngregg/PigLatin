def word_pig_latin(word):
    split = list(word)   
    if "a" not in word and "e" not in word and "i" not in word and "o" not in word and "u" not in word:
        return "a" + word + "ay"    
    elif split[0] == "a" or split[0] == "e" or split[0] == "i" or split[0] == "o" or split[0] == "u":
            return word + "way"    
    else:
        out = ""
        for i in range(len(split)):
            if split[i] != "a" and split[i] != "e" and split[i] != "i" and split[i] != "o" and split[i] != "u":
                out+= split[i]
            else:
                break
        return word[i:] + "a" + out + "ay"    

def to_pig_latin(sentence):
    sentence = sentence.split()
    out = ""
    for i in range(len(sentence)):
        out+= word_pig_latin(sentence[i]) + " "
    return out
    
def word_english(word):
    split = list(word)
    if word[-3:].endswith("way"):
        return word[:-3]
    else:
        word = word[:-2]
        split = list(word)
        out = ""
        for i in reversed(range(len(split))):
            if split[i] != "a":
                out+= split[i]
            else:
                break        
        out = out[::-1]
        return out + word[:i]

def to_english(sentence):
    sentence = sentence.split()
    out = ""
    for i in range(len(sentence)):
        out+= word_english(sentence[i]) + " "
    return out    