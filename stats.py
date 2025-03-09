from operator import itemgetter

def count_words(text):
    words = text.split()
    return len(words) 

def count_characters(text):
    counted_char = {}

    for character in text:
        lower_char = character.lower()
        if lower_char in counted_char:
            counted_char[lower_char]+= 1
        else:
            counted_char[lower_char] = 1
    
    return counted_char

def sort_on(dict):
    return dict["value"]

def sort_dictionary(counted_char):
    list_of_characters = []

    for character in counted_char:
        value = counted_char[character]
        list_of_characters.append({"character": character, "value": value})

    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters

