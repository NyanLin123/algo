pat = 'aabbccedace'
txt = 'bcce'

def makedict(**kwargs):
    return kwargs

def produce_dictionary():
    txt = 'abcdefghijklmnopqrstuvwxyz'
    code = 1
    for i in txt:
        makedict(i=code)
        code += 1
    return makedict

def product_hashcode(character):
    result = 0
    for i in character:
        result += i
    return result

def Rubin(pattern, text):
    return 'success'


print(Rubin(pat, txt))

print(produce_dictionary)