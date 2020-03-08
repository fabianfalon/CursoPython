def mi_decorador(func):
    def mi_funcion():
        print("Vamos a realizar un cálculo")
        func()
        print("Hemos realizado nuestro cálculo")

    return mi_funcion


@mi_decorador
def suma():
    print(10 + 4)


def resta():
    print(10 - 4)


suma()
print("________________________")
print("________________________")
resta()
