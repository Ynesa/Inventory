def ID_check(ID_code):
    if (all(x == ID_code[0] for x in ID_code)) or len(ID_code) < 8 or len(ID_code) > 11:
        return False
    ID_code = ('00' + ID_code)[-10:]
    intlist = [int(i) for i in ID_code]
    control = sum(intlist[ind] * (10 - ind) for ind in range(9)) % 11
    return (control if control < 2 else (11 - control)) == intlist[-1]
input("Enter Your ID Code Number: ")