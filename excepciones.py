# custom exception
class ValorIncorrecto(Exception):
    def __init__(self, val):
        print("valor {} no permitido".format(val))


def check_value():
    val = 16
    if 5 < val > 9:
        raise ValorIncorrecto(val)


check_value()
