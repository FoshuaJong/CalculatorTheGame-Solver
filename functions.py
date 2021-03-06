def call_function(number, f, x):
    try:
        n, text = f(number, x)
    except TypeError:
        n, text = f(number)

    return n, text


def add(number, addition):
    text = "add {}".format(addition)
    number = number + addition

    return number, text


def sub(number, subtraction):
    text = "subtract {}".format(subtraction)
    number = number - subtraction

    return number, text


def div(number, division):
    text = "divide by {}".format(division)
    number = number / division

    return number, text


def mul(number, multiplication):
    text = "multiply by {}".format(multiplication)
    number = number * multiplication

    return number, text


def rem(number):
    text = "remove (<<)"
    temp = str(number)

    if len(temp) == 1:
        number = 0

    temp = temp[0:-1]

    try:
        number = int(temp)
    except ValueError:
        number = 0

    return number, text


def ins(number, x):
    text = "insert {}".format(x)
    if number == 0:
        if x == 0:
            return number, text
        else:
            return x, text
    temp = str(number) + str(x)
    number = int(temp)

    return number, text


def rep(number, replacements):
    text = "replace {} with {}".format(replacements[0], replacements[1])
    temp = str(number)
    old = str(replacements[0])
    new = str(replacements[1])
    number = int(temp.replace(old, new))

    return number, text


def mypow(number, exp):
    text = "raise to power {}".format(exp)
    number = pow(number, exp)

    return number, text


def inv(number):
    text = "invert (+/-)"
    number = -1 * number

    return number, text


def rev(number):
    text = "Reverse"

    temp = str(number)

    if number >= 0:
        temp = temp[::-1]
        number = int(temp)
    else:
        temp = temp[:0:-1]
        try:
            number = int(temp) * -1
        except ValueError:
            number = 0

    return number, text

def mysum(number):
    text = "sum"
    sum = 0

    temp = str(number)

    temp.replace("-","")

    for t in temp:
        sum += int(t)

    return sum, text