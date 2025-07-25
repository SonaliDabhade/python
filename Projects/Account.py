class Account:
    def createBankAcc(self,acc_no,name,balence):
        self.acc_no=acc_no
        self.name = name
        self.balence = balence
        print("Bank Account Created ")
    
    def showDetails(self):
        print("Account Number :",self.acc_no)
        print("Accountant Name  :",self.name)
        print("Accountant Balence  :",self.balence)

    def withdrawCash(self):
        amt = int(input("Enter Amount :"))
        if amt >self.balence:
            print("Enter Sufficient Balence ")
        else:
            self.balence-=amt
            print(f"Amount of Rs.{amt} withdarwn successfully ")

    def depositCash(self):
        amt = int(input("Enter Amount :"))
        self.balence+=amt
        print(f"Amount of Rs.{amt} Deposited successfully ")

a1 = Account()
a1.createBankAcc(1001,"Jhon",1000)

a1.showDetails()

a1.depositCash()
a1.showDetails()
a1.withdrawCash()
a1.showDetails()

