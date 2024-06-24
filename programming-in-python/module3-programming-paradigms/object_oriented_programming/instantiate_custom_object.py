# class Recipe:
#     def __init__(self, dish, items, time) -> None:
#         self.dish = dish
#         self.items = items
#         self.time = time

#     def contents(self):
#         print(f"The {self.dish} has {self.items} and takes {self.time} minutes to cook.")
        

# pizza = Recipe("Pizza", ["dough, cheese, sauce"], 30)
# pasta = Recipe("Pasta", ["penne, sauce"], 55)

# print(pizza.items)
# print(pasta.items)
# pizza.contents()


# exercise 
class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index) # this is the same as self.index!
        print(f"{philosopher} wrote the book: {book}")


whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
