from clasepython.model.car import Car

def main():

    carro1: Car = Car("Nissan",2020,5)

    carro1.move(2)
    carro1.vel(True)

    print(carro1.distance_traveled)
    print(carro1.__velocidad)


if __name__ == "__main__":
    main()


