def call_function(number, f, x):
    try:
        n, text = f(number, x)
    except TypeError:
        n, text = f(number)

    return n, text


def add(number, addition):
    return number + addition, "add {}".format(addition)


def sub(number, subtraction):
    return number - subtraction, "subtract {}".format(subtraction)


def div(number, division):
    return number / division, "divide {}".format(division)


def mul(number, multiplication):
    return number * multiplication, "multiply {}".format(multiplication)


def rem(number):
    temp = str(number)

    if len(temp) == 1:
        return 0, "remove"

    temp = temp[0:-1]
    number = int(temp)

    return number, "remove"


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







