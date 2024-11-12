# Aizhamal Rysbaeva
# Nov 12, 2024

# Problem 5
# Given the following working code,
# create your own character named after yourself
# give you’re the following items and weakness
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

jama = character("Aizhamal", ["rope", "pen", "paper", "idea"], [
                 "slow", "confusion"])
print(f"my nickname is {jama.nickname}")
# print(f"my nickname is {jama.get_model()}")
print("coat" in jama.nickname)
