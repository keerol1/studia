
def bmi(waga, wzrost):
    return round(int(waga)/float(wzrost)**2, 1)

def status(bmi):
    message = ""
    if bmi(waga, wzrost)<18.5:
        message = "niedowaga"
    elif bmi(waga, wzrost)<25 and bmi(waga, wzrost)>=18.5:
        message = "waga prawidłowa"
    elif bmi(waga, wzrost)<=30 and bmi(waga, wzrost)>25:
        message = "nadwaga"
    elif bmi(waga, wzrost)>30:
        message = "otyłość"
    return message

if __name__ == '__main__':
    wzrost = input("Napisz swój wzrost (w m): ")
    waga = input("Napisz swoją wagę (w kg): ")
    print(f"Twoje bmi to {bmi(waga, wzrost)} - {status(bmi)}")
    
    
