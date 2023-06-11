kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

new_team = []

class Player:
    def __init__(self, person):
        self.name = person["name"]
        self.age = person["age"]
        self.position = person["position"]
        self.team = person["team"]
        new_team.append(self.name)

player1 = Player(kyrie)
player2 = Player(kevin)
player3 = Player(kevin)

print(new_team)





