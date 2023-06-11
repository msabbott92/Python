class user: 
    def __init__(self, firstName, lastName, email, age) -> None:
        self.first_name = firstName
        self.last_name = lastName
        self.email = email  
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0 

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount <= 0:
            print("not enough points")
        else:
            self.gold_card_points -= amount
        return self



user1 = user("Matthew", "Abbott", "me@email.com", 30)
user2 = user("Dave", "Abbott", "dave@email.com", 35)
user3 = user("Sarah", "Abbott", "sarah@email.com", 28)


user1.enroll().spend_points(80).display_info()
user2.enroll().spend_points(250).display_info()
user3.display_info()



