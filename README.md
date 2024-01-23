# PigLatin
 
To convert from English to Pig Latin, each word must be transformed as follows:
- If the word begins with a vowel, ‘way’ should be appended (example: ‘apple’ becomes ‘appleway’)
- If the word begins with a sequence of consonants, this sequence should be moved to the end, prefixed with ‘a’ and followed by ‘ay’ (example: ‘please’ becomes ‘easeaplay’)

When reverting Pig Latin to English, it is assumed that the original English text does not contain the letter "w".

# piglatin.py 

Contains the following functions:

- to_pig_latin(sentence)
Return the Pig Latin sentence for a given English sentence.

- to_english(sentence)
Return the English sentence for a given Pig Latin sentence.