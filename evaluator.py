"""
Here's the application flow - 

1. The accepted user string is sent to the tokenizer
2. A list containing the tokens are returned
3. Finally, this file evaluator.py processes the list and evaluates the expression
"""


from random import choice
from tokenizer import getTokenizedStack
from sys import argv


def concatenate(words):

    ans = ""

    for word in words:
        ans = word

    return ans


def join(words):

    return words[-1].join(words[:-1])


def pickRandom(words):

    return choice(words)


def evaluateExpression(s):
    myTokenizedStck = getTokenizedStack(s)
    ans = ""
    stck = []

    for functions in myTokenizedStck:

        if functions.key == "join":
            if len(functions.val) == 0:
                ans = join(stck)
                stck = []
            else:
                ans = join(functions.val)
                stck.append(ans)

        elif functions.key == "concatenate":
            if len(functions.val) == 0:
                ans = concatenate(stck)
                stck = []
            else:
                ans = concatenate(functions.val)
                stck.append(ans)

        elif functions.key == "pickRandom":
            if len(functions.val) == 0:
                ans = pickRandom(stck)
                stck = []
            else:
                ans = pickRandom(functions.val)
                stck.append(concatenate(functions.val))

    return ans


def isValidStrLiteral(str):
    return str.count("'") % 2 == 0 and (str[0] == "'" and str[-1] == "'")


# expr = "concatenate(pickRandom('Fruits: '), join('apple', 'grape', 'banana', 'orange', ', '))"
# expr = "pickRandom(concatenate(pickRandom('stupid')), concatenate('fax'))" # -- FAILS
# expr = "join(concatenate('hola'), join('apple', 'grape', 'banana', 'orange', ', '), '^_^')" # -- FAILS
# expr = "concatenate('bhalo', concatenate('theko'))"
# expr = "concatenate(concatenate('bhalo'), ' ', 'theko')" # -- FAILS
# expr = "concatenate('Hello', ' ', pickRandom('Pritabrata', 'Ravi', 'Ramana'))"
# expr = "concatenate(foo(), 'Fruits: ', join('apple', 'grape', 'banana', 'orange', ', '))"

expr = str(argv[1])

if expr.startswith("'"):
    if isValidStrLiteral(expr):
        print(expr)
    else:
        print(
            "You've entered an invalid string literal. a string literal is any set of characters except single quote between a pair of single quotes"
        )

try:
    print(evaluateExpression(expr))
except Exception as e:
    print(e)
