
from cmath import sqrt


def qeq(a,b,c):
    if a == 0 :
        print("Nie mozesz dzielic przez 0 chuju")      
    else:
        message = "(-b+sqrt(b**2-4*a*c))/(2*a) or (-b-sqrt(b**2-4*a*c))/(2*a)"  
        return message
    
if __name__ == "__main__":
    a = input(" Napisz a: ")
    b = input(" Napisz b: ")
    c = input(" Napisz c: ")
    print(qeq(float(a),float(b), float(c)))


