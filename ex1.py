ls_ex1 = [71, 55, 30, 42, 25, 68, 15]
#1
if ls_ex1 [2] %5 == 0:
    print("Cet élément est divisible par 5.")
else:
    print("Cet élément n'est pas divisible par 5.")
#2
if ls_ex1 [6] %2 == 0 :
    print("l'element est pair")
else:
    print("l'element n'est pas pair")
#3
if ls_ex1 [1] %2 != 0:
    print("l'element est impair")
else:
    print("l'element n'est pas impair")
#4
ls_ex1 [0] = 100
print(ls_ex1)
#5
element1 = ls_ex1[2]
element2 = ls_ex1[5]
element1, element2 = element2, element1
print(ls_ex1)
#6
ls_ex1.sort()
print(ls_ex1)
#7
ls_ex1.reverse()
print(ls_ex1)
#8
ls_ex1.index(68)
print(ls_ex1)
#9
len(ls_ex1)//2
print(ls_ex1)







