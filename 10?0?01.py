from collections import deque
a='10?0?01?'
d=deque()
d.append(a)
while(d):
    str=d.pop()
    index = str.find('?')

    if(index!=-1):

        s=str.replace('?','0',1)
        d.append(s)
        s=str.replace('?','1',1)
        d.append(s)

    else:
        print(str)
TC=O(n)
SC=O(n)
