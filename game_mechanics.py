import random

# RPG Character Class
class Character:
    def __init__(self, name, health, att_pow, defense, lvl):
        self.name = name
        self.health = health
        self.max_health = health
        self.att_pow = att_pow
        self.defense = defense
        self.lvl = lvl
        self.xp = 0
        self.xp_to_next_level = 100

    def attack(self, target):
        # Dodge chance: 10%
        if random.randint(1, 10) == 1:
            print(f"{target.name} dodged the attack!")
            return

        # Random attack power (±20%)
        random_att_pow = random.randint(int(self.att_pow * 0.8), int(self.att_pow * 1.2))

        # Critical hit chance: 20%
        if random.randint(1, 5) == 1:
            random_att_pow *= 2
            print("💥 CRITICAL HIT! 💥")

        # Calculate damage
        damage = max(1, random_att_pow - target.defense)
        print(f"{self.name} attacks {target.name} for {damage} damage")
        target.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 1:
            print(f"{self.name} has been defeated!!!")
        else:
            print(f"{self.name}'s health: {self.health}")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} XP!")

        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.lvl += 1
        self.xp = 0
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.att_pow += 5
        self.defense += 2
        self.max_health += 20
        self.health = self.max_health
        print(f"\n🎉 {self.name} leveled up to level {self.lvl}!")
        print(f"💪 Attack Power: {self.att_pow}, 🛡️ Defense: {self.defense}, ❤️ Health: {self.health}")

# **Enemy Progression (Weakest → Strongest)**
enemies = [
    ("Slime", 30, 5, 1, 1, 20),
    ("Wolf", 50, 10, 3, 2, 40),
    ("Goblin", 75, 15, 5, 3, 60),
    ("Low-level Orc", 100, 20, 8, 4, 80),
    ("Mid-level Orc", 150, 25, 10, 5, 100),
    ("Knight", 200, 30, 15, 6, 150),
    ("High-level Orc", 250, 35, 18, 7, 200),
    ("Elite Knight", 300, 40, 20, 8, 250),
    ("Orc Lord", 400, 50, 25, 9, 300),
    ("Low-level Dragon", 450, 55, 28, 10, 350),
    ("Mid-level Dragon", 500, 60, 30, 11, 400),
    ("General Knight", 550, 65, 35, 12, 450),
    ("Ancient Dragon", 600, 70, 40, 13, 500),
    ("Paladin", 700, 80, 50, 14, 600),
    ("Fire Guardian - Moltres", 800, 90, 55, 15, 700),
    ("Ice Guardian - Articuno", 800, 90, 55, 15, 700),
    ("Thunder Guardian - Zapdos", 800, 90, 55, 15, 700),
    ("Protector of Time - Dialga", 1000, 100, 60, 16, 800),
    ("Protector of Space - Palkia", 1000, 100, 60, 16, 800),
    ("Protector of Dark Matter - Giratina", 1100, 110, 65, 17, 900),
    ("The Creator - Arceus", 1500, 150, 80, 20, 1500)
]

# Create Player
player = Character("Hero", 100, 20, 5, 1)

# **Fight through all enemies one by one**
for enemy_data in enemies:
    enemy = Character(*enemy_data[:5])  # Create enemy from list
    enemy_xp_reward = enemy_data[5]

    print(f"\n⚔️ A new enemy appears: {enemy.name}! ⚔️")

    # Randomly decide who attacks first
    turn = random.choice(["player", "enemy"])

    # **Battle Loop**
    while player.health > 0 and enemy.health > 0:
        if turn == "player":
            action = input("\nType 'attack' to attack: ").lower()
            if action == "attack":
                player.attack(enemy)
                turn = "enemy"
            else:
                print("❌ Invalid action! Type 'attack' to attack.")
        else:
            enemy.attack(player)
            turn = "player"

    # **If player wins, gain XP and move on**
    if player.health > 0:
        print(f"\n🏆 {player.name} defeated {enemy.name}! 🏆")
        player.gain_xp(enemy_xp_reward)
    else:
        print(f"\n💀 {player.name} was defeated by {enemy.name}... Game Over.")
        break  # End game if player loses

# **Final Victory Message**
if player.health > 0 and enemy.name == "The Creator - Arceus":
    print("\n🌟 **Congratulations! You defeated Arceus and became the ultimate warrior!** 🌟")
