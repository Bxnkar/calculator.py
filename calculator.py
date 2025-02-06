class Calc:
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2


    def add(self):
        print(f'Ans: {self.num1 + self.num2}')
    def sub(self):
        print(f'Ans: {self.num1 - self.num2}')
    def mul(self):
        print(f'Ans: {self.num1 * self.num2}')
    def div(self):
        try:
            print(f'Ans: {self.num1 / self.num2}')
        except ZeroDivisionError as ZDE:
            print(f'{ZDE} is not possible')
while True:
    print('''calculator.py
1> Addition
2> Subtraction
3> Multiplication
4> Division
5> Quit
    ''')
    try:
        options = [1,2,3,4]
        response = int(input('> '))
        if response in options:
            num1 = int(input('1st Number: '))
            num2 = int(input('2nd Number: '))
            c = Calc(num1, num2)
        elif response == 5:
            print('closing....')
            exit()
        else:
            print('invalid input')
            if response == 1:
                c.add()
            elif response == 2:
                c.sub()
            elif response == 3:
                c.mul()
            elif response == 4:
                c.div()

    except KeyboardInterrupt:
        print('closing....')
        exit()
    except Exception as e:
        print('there must be a problem')