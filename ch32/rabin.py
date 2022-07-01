from math import prod


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

def rabin(pat, txt):

    match_code = produce_char_code(character)
    
    m = len(pat)
    n = len(txt)

    for i in range(m-n+1):
        j = 0
        if txt[j] == pat[i]:
            count += 1

rabin(pat, txt)
