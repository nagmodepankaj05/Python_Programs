accounts = { }

print(accounts)

while True:
    print("Enter Account Operation : 1. Saving Account,\n 2. deposite Money, \n 3. withdraw Money, \n 4. check balance, \n 5. Exit")

    choice =  int(input("Enter Your Choice : "))

    match(choice):
        case 1 : 
            print("Saving Account")
            n = int(input("Enter Account Number : "))
            cName = input("Enter Customer Name : ")
            cDOB = input("Enter Customer DOB : ")
            gender = input("Enter customer gender : ")
            balance = int(input("Enter Deposite : "))
            accounts[n] = {
                "name" : cName,
                "cDOB" : cDOB,
                "gender" : gender,
                "balance" : balance
            }
            
        case 2 :
            print("Deposite Money")
            n = int(input("Enter account Number : "))
            if n in accounts:
                print("Current Balance : ", accounts[n]["balance"])
                deposite = int(input("Enter deposite amount : "))
                newBalance = accounts[n]["balance"] + deposite
                accounts[n]["balance"] = newBalance
            else :
                print("Account not Exits/ Enter correct account number")

        case 3:
            print("Withdrow Money")
            n = int(input("Enter account Number : "))
            if n in accounts:
                print("Current Balance : ", accounts[n]["balance"])
                withdraw = int(input("Enter withdraw amount : "))
                newBalance = accounts[n]["balance"] - withdraw
                accounts[n]["balance"] = newBalance
            else :
                print("Account not Exits/ Enter correct account number")
        case 4:
            print("Check Balance:")
            n = int(input("Enter account Number : "))
            if n in accounts:
                print("Customer Name : ", accounts[n]["name"])
                print("Current Balance : ", accounts[n]["balance"])
        case 5:
            break
            

