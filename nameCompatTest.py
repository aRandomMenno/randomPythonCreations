
import random

nameList = ['insert', 'names', 'here']
print(' ')

def nameCompat(names):
    for j, name1 in enumerate(names):
        for i, name2 in enumerate(names):
            if j == i:
                pass
            else:
                random.seed(name1 + name2)
                score1 = random.randint(0, 100)
                random.seed(name2 + name1)
                score2 = random.randint(0, 100)
                
                # if score1 and score2 < 60:
                #     pass
                if score1 <= score2:
                    print(name1, str(score2)+'%', name2)
                elif score1 >= score2:
                    print(name1, str(score1)+'%', name2)
                elif score1 == score2:
                    print(name1, str(score1)+'%', name2)
        print(' ')

nameCompat(nameList)
