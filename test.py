while True:
    try:
        Balance = int(input("Deposit: "))
        if Balance < 0:
            print("Choose a Valid Number!!!")
            raise ValueError
        else:
            break
    except ValueError:
        print("Choose a Valid Number!!")
        pass



def b(balance):
    match = int(input("Enter: "))
    if len(balance) == 1 and match > balance[0]:
        print("True")
    else:
        print("False")
b([Balance])