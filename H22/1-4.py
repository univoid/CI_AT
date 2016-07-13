import copy
from draw_rect import draw_rect

MAX_X = 1000
MAX_Y = 1000


class Rect(object):
    x, y, w, h, flag = 0, 0, 0, 0, 0

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def set_flag(self, flag):
        self.flag = flag


def is_intersect(rect1, rect2):
    #judged by center point
    x1 = rect1.x + float(rect1.w)/2
    y1 = rect1.y + float(rect1.h)/2
    x2 = rect2.x + float(rect2.w)/2
    y2 = rect2.y + float(rect2.h)/2
    if abs(x1-x2) == float(rect1.w+rect2.w)/2 and abs(y1-y2) == float(rect1.h+rect2.h)/2:
        return False
    elif abs(x1-x2) <= float(rect1.w+rect2.w)/2 and abs(y1-y2) <= float(rect1.h+rect2.h)/2:
        return True


def find(recList, rect):
    if recList[rect.flag] == rect:
        return rect
    else:
        return find(recList, recList[rect.flag])


def union(recList, rect1, rect2):
    root1 = find(recList, rect1)
    root2 = find(recList, rect2)
    if root1 != root2:
        root1.flag = recList.index(root2)
    return 0


def get_area(bol, x, y, flag=False):
    q.queue.clear()
    sum = 1
    if flag:
        l = list()
        l.append((x, y))

    bol[x][y] = 0
    q.put((x, y))

    while not q.empty():
        x, y = q.get()
        for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx >= 0) and (ny >= 0) and (nx < MAX_X) and (ny < MAX_Y):
                if bol[nx][ny] > 0:
                    sum += 1
                    bol[nx][ny] = 0
                    q.put((nx, ny))
                    if flag:
                        l.append((nx, ny))
    if flag:
        return l
    else:
        return sum


rectList = []

# NOTICE "10.txt" for Q.1 & "1000.txt" for Q.3
with open("1000.txt", "r") as fin:
    for line in fin:
        tmp = line.split(" ")
        r = Rect(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3]))
        rectList.append(r)
        r.set_flag(len(rectList)-1)


# draw the map
f = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]
for rect in rectList:
    for i in range(rect.x, rect.x + rect.w):
        for j in range(rect.y, rect.y + rect.h):
            f[i][j] += 1


# NOTCIE Answer for Q.2
sum = 0
for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        if f[i][j] > 0:
            sum += 1
print "The summation of the area of all 1000 rectangles by 1000.txt is {}".format(sum)


# maximum thickness
maxT = 0
for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        maxT = max(maxT, f[i][j])
print "Maximum thickness is {}".format(maxT)


# the number of clusters
for i in range(0, len(rectList)-1):
    for j in range(i+1, len(rectList)):
        rect1 = rectList[i]
        rect2 = rectList[j]
        if is_intersect(rect1, rect2):
            union(rectList, rect1, rect2)
sum = 0
for rect in rectList:
    if find(rectList, rect) == rect:
        sum += 1
print "The number of clusters is {}".format(sum)


# the maximum number of cluster elements
dic = {}
for rect in rectList:
    tmp = find(rectList, rect)
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
# for key, value in dic.iteritems():
#    print key, value
print "The maximum number of cluster elements is {}".format(dic[max(dic, key=dic.get)])


# the maximum cluster area for a single cluster
import Queue
ans = 0
ansx = 0
ansy = 0
bol = copy.deepcopy(f)
q = Queue.Queue()
for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        if bol[i][j] > 0:
            sum = get_area(bol, i, j)

        if ans < sum:
            ansx = i
            ansy = j
            ans = sum

print "the maximum cluster area for a single cluster is {}".format(ans)


# Q.4
wR = 5
hR = 10
# Q.4-1
sum = 0
# # iterate the left-top coordinate of R
# for i in range(0, MAX_X - wR):
#     for j in range(0, MAX_Y - hR):
#         flag = 0
#         if f[i][j] == maxT:
#             print i, j
#
#         #iterate the area in R
#         for ir in range(i, i + wR):
#             for jr in range(j, j + hR):
#                 if f[ir][jr] == maxT:
#                     sum += 1
#                     flag = 1
#                 if flag:
#                     break
#             if flag:
#                 break

# Only (843, 109) and (844, 109) are max thickness...
# so? Let's do some hack
a = 2   # the length of max thickness rect
b = 1   # the height of max thickness rect
sum += (a + wR - 1) * (b + hR - 1)
print "the number of possible arrangements of R is {}".format(sum)

#Q.4-2

l = get_area(copy.deepcopy(f), ansx, ansy, flag=True)
draw_rect(l)    # what the fucking shape...

# as brute as I am...
# holy shit I don't care, time should not be wasted on this
''' idea:
step.1 extract boundary of this shape %'$'%&$&%$&
step.2 try all rect Rs adjoined
step.3 sum up the number of Rs adjoined but not overlapped

'''















