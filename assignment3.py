def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for letter in string:
        if letter not in vowels:
            new_string += letter
    return new_string
