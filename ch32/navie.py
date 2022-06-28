pat = 'abcdacedeacd'
txt = 'abc'

def nav(pattern, text):
    abs_pat = len(pattern)
    abs_txt = len(text)

    for i in range(abs_pat-abs_txt+1):
        # for j in range(abs_txt):
            
        print(pattern[i])


nav(pat, txt)