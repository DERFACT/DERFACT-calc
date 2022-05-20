import sys
arg = sys.argv
mat = '1234567890. +-*/%()'
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

def calc(expression):
    expression = ''.join(expression)
    if not expr_errors(expression):
        result = eval(expression)
        if (result % 1) == 0:
            result = int(result)
        print(str(result))
    else:
        print('Error: incorrect expression')

if  len(arg) > 1:
    arg.pop(0)
    results = []
    if arg[0] == '-m':
        arg.pop(0)
        for expr in arg:
            if not expr_errors(expr):
                r = eval(expr)
                if (r % 1) == 0:
                    r = int(r)
                results.append(r)
            else:
                results.append('error')
        for i in range(len(arg)):
            print(str(arg[i]) + '=' + str(results[i]))
    else:
        calc(arg)
else:
    print('DERFACT-calc v1.1 final \nCopyright (c) 2022 DERFACT Corporation')
    while True:
        expression = input('>>> ')
        calc(expression.replace(' ', ''))