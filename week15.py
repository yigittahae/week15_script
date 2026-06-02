import random

chamber_list = []
alives = []
dead = ""
for i in range (6):
    choosen = input('type prisoner name : ')
    print('{} go to gas chamber.'.format(choosen))
    chamber_list.append(choosen)
#print(chamber_list)

gun_fired = False
r = random.randint(1,6)

cycle = 1
print('the ss captain prepared the gun. game is on !')
while gun_fired == False :
    if cycle==r:
        print('the gun fired. {} died '.format(chamber_list[cycle-1]))
        died = chamber_list[cycle-1]
        gun_fired=True

    else:
        print('{} is alive. {}s turn '.format(chamber_list[cycle-1],chamber_list[cycle]))
        alives.append(chamber_list[cycle-1])
        cycle +=1
