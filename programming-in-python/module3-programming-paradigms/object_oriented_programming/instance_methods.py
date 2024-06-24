class PaySlips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return f"{self.name} has been paid {self.amount}"
        else:
            return f"{self.name} has not been paid yet"
        

nathan = PaySlips("Nathan", "no", 1000)
roger = PaySlips("Roger", "no", 3000)

print(nathan.status())
print(roger.status())

nathan.pay()

print('Afer payment')
print(nathan.status())
print(roger.status())
