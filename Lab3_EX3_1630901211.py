#ผมนำโค้ดจากในหลายเวปไซต์มาใช้editร่วมกัน ลองเขียนเองแล้วแต่เกิดerrorหลายจุดเนื่องจากเงื่อนไขที่ผิด
import re
PCD = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def infixToPostfix(exp):
    stack = []
    postfix = []
    boxes = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", exp)

    for slot in boxes:

        if slot.isalnum():
            postfix.append(slot)
        elif slot == '(':
            stack.append(slot)
        elif slot == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()
        else:
            while stack and (PCD[stack[-1]] >= PCD[slot]):
                postfix.append(stack.pop())
            stack.append(slot)
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)


print("Equations A+B")

expressions = ['A+B']
for exp in expressions:

    print("Result is : ",infixToPostfix(exp))
    print("---------------------")
    print("Equations A-B")
    expressions = ['A-B']
    for exp in expressions:

        print("Result is : ",infixToPostfix(exp))
        print("---------------------")
        print("Equations A+B-C")
    expressions = ['A+B-C']
    for exp in expressions:
        print("Result is : ",infixToPostfix(exp))
        print("---------------------")
        print("Equations A * B")
        expressions = ['A * B']
        for exp in expressions:
            print("Result is : ",infixToPostfix(exp))
            print("---------------------")
            print("Equations (A + B)* C")
        expressions = ['(A + B)* C']
        for exp in expressions:
            print("Result is : ",infixToPostfix(exp))
            print("---------------------")
            print("Equations A * (B + C)")
        expressions = ['A * (B + C)']
        for exp in expressions:
            print("Result is : ",infixToPostfix(exp))
