def Expression(stringExpresion):
    digits = []; operators = [];str = 0

    while str < len(stringExpresion):
        c=stringExpresion[str]
        if c == '(':
            operators.append(stringExpresion[str])
        elif c == ')':
            while len(operators) != 0 and operators[-1] != '(':
                value=ArithmeticOperation(digits.pop(), digits.pop(), operators.pop())
                digits.append(value)
            operators.pop()
        elif c.isdigit():
            num = 0
            while (str < len(stringExpresion) and stringExpresion[str ].isdigit()):
                num = (num * 10) + int(stringExpresion[str])
                str  =str+ 1
            digits.append(num)
            str =str-1
        else:
            while (len(operators) != 0 and check(operators[-1]) >=check(stringExpresion[str ])):
                value=ArithmeticOperation(digits.pop(), digits.pop(), operators.pop())
                digits.append(value)
            operators.append(stringExpresion[str])
        str=str+ 1
    while len(operators) != 0:
        value=ArithmeticOperation(digits.pop(), digits.pop(), operators.pop())
        digits.append(value)
    return digits[-1]
def ArithmeticOperation(op1, op2, op):
    if op == '+':
        ans= op2 + op1
        return ans
    if op == '-':
        ans= op2 - op1
        return ans
    if op == '*':
        ans= op2 * op1
        return ans
    if op == '/':
        ans= op2 // op1
        return ans

def check(operator):
    if operator=='+' :
        return 1
    if operator=='-':
        return 1
    if operator=='*' :
        return 2
    if operator=='/':
        return 2

    return 0

s=input("Enter the string:")
s=s.replace(" ","")
openbraces=s.count('(')
closedbraces=s.count(')')
s1=any(c.isalpha() for c in s)
if s1==True:
    print("alphabets are not allowed ")
    exit()
if openbraces==closedbraces:
    print(Expression(s))
else:
    print('expresseion braces does not match')
