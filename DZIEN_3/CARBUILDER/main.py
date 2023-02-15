from cbuilder import Jeep,Director

def main():
    jeepBuilder = Jeep()
    director = Director()
    print("samochów -> Jeep Cherokee")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
    print("\n")

if __name__ == '__main__':
    main()
