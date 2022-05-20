import sys
arg = sys.argv
mat = '1234567890. +-*/%'
operations = ['+', '-', '*', '/', '%', '**', '//']
commands = ['exit', 'Exit', 'exit()']
result = 0

def expr_errors(expression):
    errors = False
    if expression[len(expression) - 1] in operations or str(expression[len(expression) - 2] + expression[len(expression) - 1]) == '/0':
        errors = True
    else:
        for test in expression:
            if test not in mat or expression in operations:
                errors = True
                break
    if errors and not(len(arg) > 1) and expression in commands:
        exit()
    return errors

if  len(arg) > 1:
    arg.pop(0)
    results = []
    if arg[0] == '-m':
        arg.pop(0)
        for expr in arg:
            if not expr_errors(expr):
                r = eval(expr)
                results.append(r)
            else:
                results.append('error')
        for i in range(len(arg)):
            print(str(arg[i]) + '=' + str(results[i]))
    else:
        expression = ''.join(arg)
        if not expr_errors(expression):
            result = eval(expression)
            print(result)
        else:
            print('Error: invalid expression passed')
else:
    while True:
        a = input('Enter the expression: ')
        b = []
        for sym in a:
            if sym != ' ':
                b.append(sym)
        c = ''.join(b)
        if not expr_errors(c):
            result = eval(c)
            print(str(result))
        else:
            print('Error: incorrect expression entered')