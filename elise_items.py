import matplotlib.pyplot as plt

import pandas as pd

class target:
    def __init__(self, maxHealth, currentHealth, armor, magicResist):
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.missingHealth = maxHealth - currentHealth
        self.armor = armor
        self.magicResist = magicResist


class Elise:

    def __init__(self, level = 1, qLevel = 0, wLevel = 0, eLevel = 0, rLevel = 0, items = []):
        self.level = level
        self.qLevel = qLevel
        self.wLevel = wLevel
        self.eLevel = eLevel
        self.rLevel = rLevel
        self.baseAD = 52 + self.level * 3
        self.baseAP = 0
        self.ad = self.baseAD
        self.ap = self.baseAP
        self.mPen = 0
        self.items = items

    def rangedQ(self, target):
        damage = 5 + (35 * self.qLevel) + target.currentHealth * (.04 + self.ap*.03/100)
        return damage

    def meleeQ(self, target):
        damage = 30 + (40 * self.qLevel) + target.missingHealth * (.08 + self.ap*.03/100)
        return damage

    def rangedW(self):
        damage = 15 + (45 * self.wLevel) + self.ap * .95
        return damage

    def meleeW(self, numSpiders):
        magicDamage = (10 * self.rLevel) + (self.ap * .3) + ((5 * self.rLevel) + (self.ap * .15)) * numSpiders 
        physicalDamage = self.ad
        return (magicDamage, physicalDamage)



    def electrocute(self):
        damage = 21.176 + (self.level * 8.824) + self.ap * .25 + (self.ad - self.baseAD) * .4
        return damage


    def zombieward(self, numWards):
        if numWards == 10:
            return 30
        else:
            return numWards * 2

    def waterwalking(self):
        ap = 3.529 + 1.471 * self.level
        return ap


    def runicEchoesSplash(self):
        damage = 0
        if self.items.contains("Runic Echoes"):
            damage = 60 + self.ap * .1
        return damage


    def madness(self, damage, stacks):
        return damage + damage*stacks*.02

    def torment(self, target, cc):
        if cc == True:
            return target.maxHealth*0.075
        return target.maxHealth*0.045
    
    
    def get_items_stats(self):
        for item in self.items:
            if item.name == "Runic Echoes":
                self.ap += item.items_stats(item.stacks)[0]
            elif item.name == "Oblivion Orb":
                self.ap += item.items_stats(item.stacks)[0]
                self.mPen += item.items_stats(item.stacks)[1]
            elif item.name == "Sorcerer's Shoes":
                self.mPen += item.items_stats(item.stacks)[1]
            elif item.name == "Haunting Guise":
                self.ap += item.items_stats(item.stacks)[0]
            elif item.name == "Liandry's Torment":
                self.ap += item.items_stats(item.stacks)[0]
            elif item.name == "Seeker's Armguard":
                self.ap += item.items_stats(item.stacks)[0]
            elif item.name == "Zhonya's Hourglass":
                self.ap += item.items_stats(item.stacks)[0]


class Item:

    def __init__(self, name, stacks = 0):
        self.name = name
        self.stacks = stacks


    def items_stats(self, stacks):
        if self.name == "Runic Echoes":
            ap = 80
            return (ap, 0)
        elif self.name == "Oblivion Orb":
            ap = 20
            mPen = 15
            return (ap, mPen)
        elif self.name == "Sorcerer's Shoes":
            mPen = 18
            return (0, mPen)
        elif self.name == "Amplifying Tomb":
            ap = 20
            return (ap, 0)
        elif self.name == "Haunting Guise":
            ap = 35
            return (ap, 0)
        elif self.name == "Liandry's Torment":
            ap = 75
            return (ap, 0)
        elif self.name == "Seeker's Armguard":
            ap = 20 + .5*self.stacks
            return (ap, 0)   
        elif self.name == "Zhonya's Hourglass":
            ap = 75
            return (ap, 0)  
        



    # def liandries(self):
    #     ap = 75
    #     madness = "2 % more damage per stack, up to 5 stacks"
    #     torment = "4.5% max health over 3 seconds, 7.5% if immobilized"

    # def seekers(self, stacks):
    #     ap = 20 + .5*stacks

    # def zhonyas(self):
    #     ap = 75

    # def voidStaff(self):
    #     ap = 80
    #     penetration = "40 percent"

    # def rabadon(self):
    #     ap = 120
    #     bonus = "40 percent ability power"




        

# sorc boots, runic echoes, oblivion                 lv 9
# sorc boots, runic echoes, haunting guise

# sorc boots, runic echoes, liandries                   lv 11
# sorc boots, runic echoes, oblivion, haunting guise

# sorc boots, runic echoes, liandries, void staff (3100 + 2650)         lv 14
# sorc boots, runic echoes, oblivion, haunting guise, void staff (1600 + 1500 + 2650)

# sorc boots, runic echoes, oblivion, void staff, zhonyas (1600 + 2900) 4500            lv 16
# sorc boots, runic echoes, liandries, void staff seekers amptomb (3100 + 1100)



def main():


    sorcBoots = Item("Sorcerer's Shoes")
    runicEchoes = Item("Runic Echoes")
    oblivion = Item("Oblivion Orb") 
    haunting = Item("Haunting Guise") 
    liandry = Item("Liandry's Torment")



    
    #self, level = 1, qLevel = 0, wLevel = 0, eLevel = 0, rLevel = 0, ad = 55, ap = 0, mPen = 0, items = [sorcBoots, runicEchoes, oblivion]):

    # sorc boots, runic echoes, oblivion, lv 9
    elise1 = Elise(9, 5, 2, 1, 2, [sorcBoots, runicEchoes, oblivion])

    elise1.get_items_stats()

    elise2 = Elise(9, 5, 2, 1, 2, [sorcBoots, runicEchoes, haunting])
    elise2.get_items_stats()


    damageList1 = []
    magicResistList1 = []

    
    damageList2 = []
    magicResistList2 = []
    nums = 200


    for i in range(nums):
        enemy1 = target(1000, 1000, 50, i + 30)
        enemy2 = target(1000, 1000, 50, i + 30)

        magicResistList1.append(enemy1.magicResist)

        magicResist1 = enemy1.magicResist - elise1.mPen
        magicDamageX1 = (elise1.rangedQ(enemy1) + elise1.rangedW() + elise1.meleeW(3)[0] + elise1.electrocute()) * 100/ (100 + magicResist1)
        physicalDamage1 = elise1.meleeW(3)[1]*100/(100 + enemy1.armor)



        enemy1.currentHealth = enemy1.currentHealth - (magicDamageX1 + physicalDamage1)
        enemy1.missingHealth = enemy1.maxHealth - enemy1.currentHealth

        magicDamageY1 = elise1.meleeQ(enemy1)*100/(100 + magicResist1)

        damage1 = magicDamageX1 + physicalDamage1 + magicDamageY1
        damageList1.append(damage1)
        



        magicResistList2.append(enemy2.magicResist)

        magicResist2 = enemy2.magicResist - elise2.mPen
        magicDamageX2 = (elise2.rangedQ(enemy2) + elise2.rangedW() + elise2.meleeW(3)[0] + elise2.electrocute()) * 100/ (100 + magicResist2)
        physicalDamage2 = elise2.meleeW(3)[1]*100/(100 + enemy2.armor)



        enemy2.currentHealth = enemy2.currentHealth - (magicDamageX2 + physicalDamage2)
        enemy2.missingHealth = enemy2.maxHealth - enemy2.currentHealth

        magicDamageY2 = elise2.meleeQ(enemy2)*100/(100 + magicResist2)

        damage2 = magicDamageX2 + physicalDamage2 + magicDamageY2
        damageList2.append(damage2*1.1)





    plt.plot(magicResistList1, damageList1, '-.', color = "chocolate")
    plt.plot(magicResistList2, damageList2, '-.', color = "green")
    plt.xlabel('MR')
    plt.ylabel('Damage')
    plt.show()




    elise3 = Elise(11, 5, 2, 1, 2, [sorcBoots, runicEchoes, oblivion, haunting])

    elise3.get_items_stats()

    elise4 = Elise(11, 5, 2, 1, 2, [sorcBoots, runicEchoes, liandry])
    elise4.get_items_stats()

    damageList3 = []
    magicResistList3 = []

    
    damageList4 = []
    magicResistList4 = []


    damageList5 = []
    magicResistList5 = []


    for i in range(nums):
        enemy1 = target(1500, 1500, 70, i + 30)
        enemy2 = target(1500, 1500, 70, i + 30)
        enemy3 = target(1500, 1500, 70, i + 30)

        magicResistList3.append(enemy1.magicResist)

        magicResist1 = enemy1.magicResist - elise3.mPen
        magicDamageX1 = (elise3.rangedQ(enemy1) + elise3.rangedW() + elise3.meleeW(3)[0] + elise3.electrocute()) * 100/ (100 + magicResist1)
        physicalDamage1 = elise3.meleeW(3)[1]*100/(100 + enemy1.armor)



        enemy1.currentHealth = enemy1.currentHealth - (magicDamageX1 + physicalDamage1)
        enemy1.missingHealth = enemy1.maxHealth - enemy1.currentHealth

        magicDamageY1 = elise3.meleeQ(enemy1)*100/(100 + magicResist1)

        damage1 = magicDamageX1 + physicalDamage1 + magicDamageY1
        damageList3.append(damage1)
        



        magicResistList4.append(enemy2.magicResist)

        magicResist2 = enemy2.magicResist - elise4.mPen
        magicDamageX2 = (elise4.rangedQ(enemy2) + elise4.rangedW() + elise4.meleeW(3)[0] + elise4.electrocute() + elise4.torment(enemy2, True)) * 100 / (100 + magicResist2)
        physicalDamage2 = elise4.meleeW(3)[1]*100/(100 + enemy2.armor)



        enemy2.currentHealth = enemy2.currentHealth - (magicDamageX2 + physicalDamage2)
        enemy2.missingHealth = enemy2.maxHealth - enemy2.currentHealth

        magicDamageY2 = elise4.meleeQ(enemy2)*100/(100 + magicResist2)

        damage2 = magicDamageX2 + physicalDamage2 + magicDamageY2
        damageList4.append(damage2)

        

        
        magicResistList5.append(enemy3.magicResist)

        magicResist3 = enemy3.magicResist - elise4.mPen
        magicDamageX3 = (elise4.rangedQ(enemy3) + elise4.rangedW() + elise4.meleeW(3)[0] + elise4.electrocute() + elise4.torment(enemy3, False)) * 100 / (100 + magicResist3)
        physicalDamage3 = elise4.meleeW(3)[1]*100/(100 + enemy3.armor)



        enemy3.currentHealth = enemy3.currentHealth - (magicDamageX3 + physicalDamage3)
        enemy3.missingHealth = enemy3.maxHealth - enemy3.currentHealth

        magicDamageY3 = elise4.meleeQ(enemy3)*100/(100 + magicResist3)

        damage3 = magicDamageX3 + physicalDamage3 + magicDamageY3
        damageList5.append(damage3)


    plt.plot(magicResistList3, damageList3, '-.', color = "chocolate")
    plt.plot(magicResistList4, damageList4, '-.', color = "green")
    plt.plot(magicResistList5, damageList5, '-.', color = "#333333")
    plt.xlabel('MR')
    plt.ylabel('Damage')
    plt.show()



    # Standard damage will be ranged q, w, melee auto, electrocute, melee q
    # Measure damage with 10% extra damage and without from liandries. 
    # Measure damage according to 3 different levels of max health of target.
    # Measure damage s
    

if __name__ == "__main__":
    main()
