from time import sleep

str = ['Position:2022, 649',
'Position:1116, 639',
'Position: 894, 609',
'Position: 935, 609',
'Position: 940, 610',
'Position: 934, 610',
'Position: 848, 606',
'Position: 822, 606',
'Position: 883, 604',
'Position:1166, 604',
'Position:1170, 604']
li = []
di = {}
for i in str:
    a = i.split('Position:')[1]
    b = a.split(', ')
    di['x'] = b[0]
    di['y'] = b[1]
    li.append(di)
print(li)