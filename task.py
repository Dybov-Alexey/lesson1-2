from math import sqrt
def diskriminant(a,b,c):
    return b*b-4*a*c
#print('Введите коэффиценты A,B,C:')
a = int(input("Введите коэффицент A: " ))
b = int(input("Введите коэффицент B: " ))
c = int(input("Введите коэффицент C: " ))
print("Уравнение: (",a,")x^2 + (",b,")x + (",c,") = 0")
if a == 0 and b !=0:
    x = -1*c/b
    if x == 0:
        print('Бесконечное множество корней')
    else:
        print('Один корень: ',x)
elif b == 0 and a == 0 and c == 0:
    print('Бесконечное множество корней')
elif b == 0 and a == 0 and c != 0:
    print(c," != 0")
    print('Некорректные данные')
else:
    d = diskriminant(a,b,c)
    if d < 0:
        print('Нет решений')
    elif d == 0:
        x = -1*b/2/a
        print('Один корень: ',x)
    else:
        x1 = (-1*b+sqrt(d))/2/a
        x2 = (-1*b-sqrt(d))/2/a
        print('Два корня: ',x1,x2)