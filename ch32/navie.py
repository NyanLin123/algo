pat = 'abcdacedeacd'
txt = 'abcda'

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
        else:
            print('fount at position end at ', j)


nav(pat, txt)