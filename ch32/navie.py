pat = 'abcdacedeacd'
txt = 'ced'


def nav(pattern, text):
    abs_pat = len(pattern)
    abs_txt = len(text)

    for i in range(abs_pat-abs_txt+1):
        j = 0
        while(j < abs_txt):
            if pattern[i+j] == text[j]:
                j += 1
            else:
                break
        if j > 2:
            print(i+1)


def speed_up(pattern, text):
    n = 0  # for pattern
    m = 0  # for text
    while n < len(pattern): #for time n
        if pattern[n] == text[m]:
            m += 1
            print(n, m)
        elif pattern[n] != text[m]:
            m = 0
            n += 1

speed_up(pat, txt)
