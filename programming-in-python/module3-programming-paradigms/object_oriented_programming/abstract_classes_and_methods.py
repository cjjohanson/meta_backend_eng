from abc import ABC, abstractmethod

class Donation(ABC):
    @abstractmethod
    def donate(self):
        # you pass because you don't implement here. instead, you are forcing
        # the child classes to implement
        pass

class Employee(Donation):
    def donate(self):
        donation_amount = input("How much would you like to donate? ")

        return donation_amount
    
donations = []

john = Employee()
john_donation = john.donate()
donations.append(john_donation)

peter = Employee()
peter_donation = peter.donate()
donations.append(peter_donation)

print(donations)



    
