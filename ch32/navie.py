pat = 'abcdacedeacd'
txt = 'ced'

def nav(pattern, text):
    abs_pat = len(pattern)
    abs_txt = len(text)

    for i in range(abs_pat-abs_txt+1):
        j = 0
        while(j<abs_txt):
            if pattern[i+j] == text[j]:
                j += 1
            else:
                break
        if j > 2:
            print(i+1)


nav(pat, txt)