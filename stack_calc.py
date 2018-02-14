ent_list = input("Введите выражение: ").split()
stack_list = []
flag_zerodiv = 0
for x in ent_list:
    print(x, stack_list)
    if x == '+':
        op2, op1 = stack_list.pop(), stack_list.pop()
        stack_list.append(op1 + op2)
    elif x == '-':
        op2, op1 = stack_list.pop(), stack_list.pop()
        stack_list.append(op1 - op2)
    elif x == '*':
        op2, op1 = stack_list.pop(), stack_list.pop()
        stack_list.append(op1 * op2)
    elif x == '/':
        op2, op1 = stack_list.pop(), stack_list.pop()
        stack_list.append(op1 / op2)
    else:
        stack_list.append(float(x))
else:
    print('Результат: {:.2f}'.format(stack_list.pop()))
