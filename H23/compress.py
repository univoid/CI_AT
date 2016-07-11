def make_dic(s):
    dic = {}
    i = 0
    while i+6 < len(s):
        if s[i:i+6] not in dic:
            val = str(i)
            while len(val) < 3:
                val = "0" + val
            dic[s[i:i+6]] = val
        i += 1
    return dic

def compress_str(s):
    dic = make_dic(s)
    s_ans = str()
    i = 0
    while i < len(s):
        substr = s[i:i+6]
        if substr in dic and int(dic[substr]) != i:
            s_ans += dic[substr]
            i += 6
        else:
            s_ans += s[i]
            i += 1
    return s_ans


