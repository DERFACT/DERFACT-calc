'''DERFACT-calc -- A simple command line calculator
   Copyright (C) 2022 DERFACT Corporation,
   DERFACT-calc is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   DERFACT-calc is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
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
