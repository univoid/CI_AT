''' idea:
step.1  initialize a queue Q
step.2  put a rectangle R into Q and set attr <deep> of R = 1
step.3  analyze all the overlapped rectangles of R with other rectangle in Q
step.4  put all those rectangle (e.g. B = R overlap A  ) into Q and set attr deep of B = max(R, A) + 1
step.5  repeat step.2~4 until all rectangles were in Q
step.6  print the final answer = max<deep>
'''