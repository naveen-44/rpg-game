from player import *
import random


def addExp(p,lvl):
    if p.level == lvl:
        p.exp += 7
    if p.level < lvl:
        val = lvl - p.level
        p.exp += ((val+1)**2)*7
    else:
        val = p.level - lvl
        p.exp += max(7 - val*3,0)
    while p.exp >= p.level*5:
        p.exp %= (p.level * 5)
        p.level += 1

def levelUp(p):
    rpg_types = ['mage','hunter','merc','no type']
    p.maxhp += 10
    p.hp = p.maxhp
    p.defence += 10
    p.attack += 10
    if p.rpg_type == rpg_types[0]:
        p.attack += 5
    elif p.rpg_type == rpg_types[1]:
        p.defence += 5
    elif p.rpg_type == rpg_types[2]:
        p.maxhp += 5
        p.hp = p.maxhp
    else:
        p.maxhp += 1
        p.hp = p.maxhp
        p.defence += 2
        p.attack += 2
    


def missChance(miss = 25):
    r = random.randint(0,100)
    return r <= miss

def aHitB(a,b):
    attack_value = a.atk*(a.attack/100)
    defence_value = b.defence - 100
    attack_value *= (100-defence_value)/100
    if not missChance():
        b.hp -= attack_value
        b.hp = round(b.hp,2)
    # print(b.name, ' took ', attack_value , ' damage')

def refresh(p):
    p.hp = p.maxhp

def fight(p1,p2):
    # play with current hp
    print(p1.name, ' vs ', p2.name)
    print(p1.hp,'/',p1.maxhp,' ', p2.hp,'/',p2.maxhp)
    while p1.hp > 0 and p2.hp > 0:
        # print(p1.name, ' hits ', p2.name)
        aHitB(p1,p2)
        # print(p2.name, ' hits ', p1.name)
        aHitB(p2,p1)
        print(p1.hp,'/',p1.maxhp,' ', p2.hp,'/',p2.maxhp)

    winner = -1
    if p1.hp <= 0 and p2.hp <= 0:
        print('its a draw!')
    elif p1.hp <= 0:
        print(p2.name, ' has won!')
        winner = 2
    else:
        print(p1.name, ' has won!')
        winner = 1

    refresh(p1)
    refresh(p2)
    # add exp
    if winner == 1:
        addExp(p1,p2.level)
    elif winner == 2:
        addExp(p2,p1.level)
    
    return winner
    


p0 = player(0,'zero')
p1 = player(1,'praveen')
p2 = player(2,'naveen')
p3 = player(3,'harish')

p0.show()
p1.show()
p2.show()
p3.show()

winner = fight(p3,p1)