# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:50:14 2019

@author: tanabe hiroki
"""

# line = 'abc\ndef'
# for li in line:
#     print(li)

# t = {'A':[5*x for x in range(12)],'B':[]}
# print(t['B']==[])

# s = '00 A1 12'
# l = s.split()
# print(str(l[1][1]))

lines = 'A A5 U 13'

t_from_A1 = {'1':0,'2':3,'3':8,'4':10,'5':13,'6':17,'7':20,'8':24,'9':26,'10':28,'11':31,'12':37,'13':39}
t_from_B1 = {'1':0,'2':4,'3':7,'4':10,'5':12,'7':15}

# t_A1AU = {'05':[55],'after06':[5*x for x in range(12)]}
t_A1AU = [5*x for x in range(12)]
t_A7AD = [6+10*x for x in range(6)] 
t_A7AU = [10]
t_A7BD = [5+6*x for x in range(10)]
t_B1BU = [6*x for x in range(10)]
t_A13AD = [2+10*x for x in range(10)]

lines_l = lines.split()

result = list(map(lambda x: (x+t_from_A1[lines_l[1][1]])%60,t_A1AU))
result.sort()
# print(result)
print('{0:04d}'.format(result))

# if (lines_l[0] == 'A') and (1<=int(lines_l[1][1])<7):
#     result = (t_A1AU + t_from_A1[lines_l[1][1]]) % 60
#     print(result)
    