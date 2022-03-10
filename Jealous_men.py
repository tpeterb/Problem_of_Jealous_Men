from Feladat import *

class Feltekeny_ferfiak(Feladat):

    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return self.cel == allapot

    def rakovetkezo(self, allapot):
        lepesek = []
        for i in range(0, 6): #The index of the first the person
            for j in range(-1, 6): #The optional index of the second person - if there's any
                tmp = True
                for k in range(0, 2): #The index of the side of the river
                    if j == -1: #Taking only one person across the river
                        if allapot[i] != k: #It makes no sense to take someone to the same place
                            if i > -1 and i < 3: #Taking only a woman across the river
                                if allapot[i + 3] == k: #If her husband is on the other side, the woman can be taken to the other side of the river
                                    tmp = True
                                    break
                                else: #If her husband isn't on the other side
                                     for f in range(3, 6):
                                        if f != i + 3 and allapot[f] != k: #If other men aren't on the other side, the woman can be taken across the river
                                            tmp = True
                                        elif f != i + 3 and allapot[f] == k: #If there are other men on the other side of the river, the woman mustn't go across the river
                                            tmp = False
                                            break
                            else: #Taking only a man across the river
                                if allapot[i - 3] != k: #If the man left his wife alone
                                    for f in range(3, 6):
                                        if f != i and allapot[f] == k: #If all other men are on the other side, then the man can be taken across the river
                                            tmp = True
                                        elif f != i and allapot[f] != k: #If there are other men left next to the chosen man's wife, the operation isn't permitted
                                            tmp = False
                                            break
                        else:
                            tmp = False #Leaving someone in place is not an operator
                    else: #Taking two people across the river
                        if allapot[i] != k and allapot[j] != k: #It makes no sense to take someone to the same place
                            if i == j: #The same person cannot be handled as two people
                                tmp = False
                            else:
                                if i in [0, 1, 2]: #If the first person is a woman
                                    if j in [3, 4, 5] and j != i + 3: #If the second person is a man, who isn't her husband, the operation isn't permitted
                                        tmp = False
                                        break
                                    if j not in [0, 1, 2]: #If only one woman is in the boat
                                        if allapot[i + 3] == k: #If the company in the boat is alright, and the woman's husband is on the other side, they can be taken across the river
                                            tmp = True
                                        elif allapot[i + 3] != k: #If her husband isn't on the other side
                                            for f in [3, 4, 5]:
                                                if f != i + 3 and allapot[f] == k: #If the woman's wife isn't on the other side and there are other men, the woman cannot be taken across the river
                                                    tmp = False
                                    if j in [0, 1, 2]: #If two women are in the boat
                                        if allapot[i + 3] == k and allapot[j + 3] == k: #If both woman's husband is on the other side, they can be taken across the river
                                            tmp = True
                                        else:
                                            for f in range(3, 6):
                                                if (allapot[i + 3] != k and f != i + 3 and allapot[f] == k) or (allapot[j + 3] != k and f != j + 3 and allapot[f] == k): #If at least one woman remained without her husband with an other man on the other side, the operation is prohibited
                                                    tmp = False
                                elif i in [3, 4, 5]: #If the first person is a man
                                    if j not in [3, 4, 5]: #The other person is a woman
                                        for f in [3, 4, 5]:
                                            if f != i and allapot[f] != k and allapot[i - 3] != k: #A man left his wife with another man
                                                tmp = False
                                                break
                                    elif j in [3, 4, 5]: #Two men are in the boat
                                        for f in [3, 4, 5]:
                                            if (f != i and f != j and allapot[f] != k and allapot[i - 3] != k) or (f != j and f != i and allapot[f] != k and allapot[j - 3] != k): #At least one wife was left alone
                                                tmp = False
                                                break
                        else:
                            tmp = False #Leaving someone in place is not an operator
                    if tmp:
                        uj_allapot = list(allapot)
                        if j == -1: #Only one person was in the boat
                            uj_allapot[i] = k
                        else: #Two people were in the boat
                            uj_allapot[i] = k
                            uj_allapot[j] = k
                        uj_allapot2 = tuple(uj_allapot)
                        lepesek.append(uj_allapot2)


if __name__ == "__main__":
    ferfiak = Feltekeny_ferfiak((0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1))
