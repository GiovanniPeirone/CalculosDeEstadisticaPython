import matplotlib.pyplot as plt

def PedirValores():
    print()

def GraficoDeTorta():
    manzanas = [5,1,25,30]
    nombres = ["Ana","Juan","Diana","Catalina"]
    plt.pie(manzanas, labels=nombres)
    plt.show()

def main():
    GraficoDeTorta()
    return 0




while True:
    #try:
        main()
    #except ValueError:
        #break