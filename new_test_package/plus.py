class CalcPlus:
    def __init__(self, *args):
        s = 0
        p = 1
        for i in args:
            s += i
            p *= i
        self.summa = s
        self.multi = p



num = CalcPlus(2, 3, 3, 3, 2, 7)
num1 = CalcPlus(5, 6, 8, 9, 3, 11, 56, 55)
num2 = CalcPlus(4, 8, 8, 4)
print(num.summa)
print(num1.summa)
print('нах')
print(num2.multi)
