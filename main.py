def alt_caps(original_string):
    new_string = ""
    make_upper = False

    for char in original_string:
        if char.isalpha():
            if make_upper:
                new_string += char.upper()
            else:
                new_string += char.lower()
            make_upper = not make_upper
        else:
            new_string += char

    return new_string

print(alt_caps("Alternating Capitalization"))