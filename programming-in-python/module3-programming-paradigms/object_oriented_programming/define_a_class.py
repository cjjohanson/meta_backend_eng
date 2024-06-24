class House:
    num_rooms = 5 # attribute
    bathrooms = 2 # attribute
    def cost_evaluation(self):
        """
        This is a method
        """
        print(self.num_rooms)
        pass

house = House()
print(f"house.num_rooms: {house.num_rooms}")
print(f"House.bathrooms: {House.num_rooms}")
House.num_rooms = 10
print(f"house.num_rooms: {house.num_rooms}")
print(f"House.bathrooms: {House.num_rooms}")