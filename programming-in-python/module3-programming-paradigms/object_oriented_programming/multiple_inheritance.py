# class A:
#     a = 1

# class B(A):
#     a = 2

# class C(B):
#     pass

# c = C()
# print(f"c.a = {c.a}")

# print(f"C a subclass of B: {issubclass(C, B)}")
# print(f"c an instance of C: {isinstance(c, C)}")

class A:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def method(self):
        print("Class A method called")

    def multiply(self):
        print(f"{self.x} * {self.y} = {self.x * self.y}")

class B(A):
    # you're extending the class by adding c even though you dont end up doing anything
    # with it!
    def __init__(self, x, y, c) -> None:
        # you still need to initialize the variable from the parent class
        super().__init__(x, y)
        self.c = c

    def method(self):
        print("Class B method")

a = A(2, 3)
b = B(20, 10, 6)
a.method()
a.multiply()
b.multiply()
b.method()
