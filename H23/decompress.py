def decompress_str(s):
    s_ans = str()
    i = 0

    while i < len(s):
        if unicode(s[i]).isdecimal():
            num = int(s[i:i+3])
            if num+6 <= len(s_ans):
                s_ans += s_ans[num:num+6]
            else:
                suffix = len(s_ans)-num
                s_ans += s_ans[num:len(s_ans)] * (6 / suffix) + s_ans[num:num + 6 % suffix]

            i += 3
        else:
            s_ans += s[i]
            i += 1

    return s_ans
