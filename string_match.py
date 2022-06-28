
text = 'abcdeeabcde'
pat = 'abc'

def search(P, T):
    x = len(P)
    y = len(T)

    for i in range(x-y):
        j = 0
        for j in range(i):
            print(i,j)

search(text, pat)