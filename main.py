class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Member(Person):
    def __init__(self, name, age, membership_type):
        super().__init__(name, age)
        self.membership_type = membership_type

    def __str__(self):
        return f"Member - {super().__str__()}, Membership Type: {self.membership_type}"


class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}"


class Gun(Item):
    def __init__(self, name, serial_number, model, quantity):
        super().__init__(name, quantity)
        self.serial_number = serial_number
        self.model = model

    def __str__(self):
        return f"Gun - Serial Number: {self.serial_number}, Model: {self.model}, {super().__str__()}"


class GunClub:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.inventory = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_name):
        for member in self.members:
            if member.name == member_name:
                self.members.remove(member)
                return True
        return False

    def add_item(self, item):
        found = False
        for existing_item in self.inventory:
            if isinstance(existing_item, type(item)) and existing_item.name == item.name:
                existing_item.quantity += item.quantity
                found = True
                break
        if not found:
            self.inventory.append(item)

    def remove_item(self, item_name, quantity):
        for item in self.inventory:
            if isinstance(item, Gun) and item.name == item_name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.inventory.remove(item)
                    return True
        return False

    def list_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            print(member)

    def list_inventory(self):
        print(f"Inventory of {self.name}:")
        for item in self.inventory:
            print(item)



if __name__ == "__main__":
    club = GunClub("Python Gun Club")

    # Added thy members
    member1 = Member("Hamid khan", 30, "Regular")
    member2 = Member("muhammad waqas", 25, "Premium")
    club.add_member(member1)
    club.add_member(member2)

    # Adding guns to stock
    gun1 = Gun("Colt Python", "SN123", "Revolver", 5)
    gun2 = Gun("Glock 17", "SN456", "Pistol", 10)
    club.add_item(gun1)
    club.add_item(gun2)

    #  club information
    club.list_members()
    club.list_inventory()

    # Remove a member
    club.remove_member("John Doe")
    club.list_members()

    # Removing guns from stock
    club.remove_item("Glock 17", 3)
    club.list_inventory()
