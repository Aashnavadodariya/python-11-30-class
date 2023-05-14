class bank:
    def openaccount(self,acno,cname,balence):
        self.acno=acno
        self.cname=cname
        self.balence=balence
        print("hello",self.cname,",your account number",self.acno,"is opened with",self.balence,"rs.")

    def deposite(self,amount):
        self.balence+amount

    def withdraw(self,amount):
        if amount<=self.balence:self.balence=self.balence-amount

        else:
            print("insufficient fund")
    def checkbalence(self):
        print("current balence :",self.balence)

b1=bank()
b1.openaccount(101,"aashna",1000)
b1.deposite(5000)
b1.checkbalence()
b1.withdraw(4000)
b1.checkbalence()
