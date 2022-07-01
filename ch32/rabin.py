
pat = 'aabbccedace'
txt = 'bcce'

character = 'abcdefghijklmnopqrstuvwxyz'

def produce_char_code(character):
    code = {}
    index = 1
    for i in character:
        code[i]= index
        index += 1
    return code

def compare_character(char_dic, single_character):
    for i in char_dic:
        if i.keys == single_character:
            return i.values()
        else:
            return "Error"

def calculation_single_code(text_pattern):
    result = 0
    for i in text_pattern:
        result += compare_character(produce_char_code(character), i)

    return result


def rabin(pat, txt):

    match_code = produce_char_code(character)

    m = len(pat)
    n = len(txt)

    for i in range(m-n+1):
        j = 0
        if compare_character(match_code, txt[j]) == compare_character(match_code, pat[i]):
            count += 1

print(produce_char_code(character).has_key('a'))
