def add_keyword(string):
    new_keywords = []
    key_word_one = string
    key_word_two = string[0].upper() + string[1:]
    key_word_three = f'"{string}"'
    key_word_four = f'"{string[0].upper()}{string[1:]}"'
    key_word_five = string.upper()
    key_word_six= f'{string}.'
    key_word_seven= f'{string[0].upper()}{string[1:]}.'
    
    words_to_add = [key_word_one,key_word_two,key_word_three,key_word_four, key_word_five,key_word_six,key_word_seven ]
    
    new_keywords.append(words_to_add)

    return new_keywords


print(add_keyword('помогите'))