
def lineq(a,b):
    try:
        return -b/a
    except:
        print("Nie mozesz dzielic przez 0 chuju")
        exit()

if __name__ == "__main__":
    a = input(" Napisz współczynnik kierunkowy: ")
    b = input(" Napisz wyraz wolny: ")
    print(lineq(float(a),float(b)))


