import sys
arg = sys.argv
mat = '1234567890. +-*/%'
operations = ['+', '-', '*', '/', '%', '**', '//']
commands = ['exit', 'Exit', 'exit()']
result = 0
if  len(arg) > 1:
    arg.pop(0)
    results = []
    if arg[0] == '-m':
        arg.pop(0)
        for expr in arg:
            errors = False
            if expr[len(expr) - 1] in operations or str(expr[len(expr) - 2] + expr[len(expr) - 1]) == '/0':
                errors = True
            else:
                for test in expr:
                    if test not in mat or expr in operations:
                        errors = True
                        break
            
            if not errors:
                r = eval(expr)
                results.append(r)
            else:
                results.append('error')
        for i in range(len(arg)):
            print(str(arg[i]) + '=' + str(results[i]))
    else:
        expression = ''.join(arg)
        errors = False
        if expression[len(expression) - 1] in operations or str(expression[len(expression) - 2] + expression[len(expression) - 1]) == '/0':
            errors = True
        else:
            for test in expression:
                if test not in mat:
                    errors = True
                    break
        if not errors:
            result = eval(expression)
            print(result)
        else:
            print('Error: invalid expression passed')
else:
    while True:
        errors = False
        a = input('Enter the expression: ')
        b = []
        for sym in a:
            if sym != ' ':
                b.append(sym)
        c = ''.join(b)
        for test in c:
            if (test not in mat or c[len(c) - 1] in operations or str(c[len(c) - 2] + c[len(c) - 1]) == '/0') and (c not in commands):
                errors = True
                break
        if not errors:
            if c in commands:
                break
            else:
                result = eval(c)
                print(str(result))
        else:
            print('Error: incorrect expression entered')