
from cmath import sqrt


def qeq(a,b,c):
    if a == 0 :
        print("Nie mozesz dzielic przez 0 chuju")
    else:
        x = (-b+sqrt(b**2-4*a*c))/(2*a)
        y = (-b-sqrt(b**2-4*a*c))/(2*a)
        return x,y
if __name__ == "__main__":
    a = input(" Napisz a: ")
    b = input(" Napisz b: ")
    c = input(" Napisz c: ")
    print(qeq(float(a),float(b), float(c)))


