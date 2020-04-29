import operator
import random as r
poker1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'Q', 'k']
poker2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'Q', 'k']
print (operator.eq(poker1, poker2))

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'Q', 'k'] * 4
print (poker)
print (len(poker))
print (poker.count('A'))

# 抽一張牌

#print('抽一張牌:' , poker.pop(0))
card = poker.pop(0)
print('抽一張牌:' , card)
print(poker)
#洗牌
r.shuffle(poker)
print(poker)

#計算前三張的點數
