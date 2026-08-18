# ==========================================
#  MY PHASE 1 CODING JOURNEY (Day 1-14)
#  by SwaggyApex - the number one Gojo main
# ==========================================

# ----- DAY 1: Variables & print -----
name = "Apex"
print("My name is", name)

# ----- DAY 2: Math -----
health = 100
damage = 30
print("Health left:", health - damage)

# ----- DAY 4: if/else -----
score = 75
if score >= 50:
    print("You win!")
else:
    print("You lose!")

# ----- DAY 5: Loops -----
for i in range(1, 6):
    print("Number:", i)

# ----- DAY 6: Lists -----
inventory = ["Gojo", "Sukuna", "Megumi"]
inventory.append("Nanami")
inventory.remove("Megumi")
print(inventory)

# ----- DAY 7: Dictionaries -----
character = {"name": "Nanami", "power": 75, "technique": "Ratio"}
print(character["name"], "has power", character["power"])

# ----- DAY 8: Strings -----
message = "the guest is awake"
print(message.upper())

# ----- DAY 9: Files -----
with open("log.txt", "w") as file:
    file.write("Day 1: normal\n")
    file.write("Day 7: the guest is awake\n")
with open("log.txt", "r") as file:
    print(file.read())

# ----- DAY 10: Caesar Cipher -----
message = "TWITCH"
shift = 3
secret = ""
for letter in message:
    secret = secret + chr(ord(letter) + shift)
print("Encoded:", secret)   # TWITCH -> WZLWFK

# ----- DAY 11: NumPy -----
import numpy as np
scores = np.array([50, 80, 30, 90])
print("Average:", scores.mean())
print("Above average:", scores[scores > scores.mean()])

# ----- DAY 12: Pandas -----
import pandas as pd
data = {"character": ["Gojo", "Mahito", "Hakari", "Todo"],
        "damage": [100, 90, 85, 23]}
df = pd.DataFrame(data)
print(df)

# ----- DAY 13 & 14: Matplotlib + Capstone -----
import matplotlib.pyplot as plt

print("Average damage:", df["damage"].mean())
print("Above average:")
print(df[df["damage"] > df["damage"].mean()])

plt.bar(df["character"], df["damage"], color=["cyan", "purple", "magenta", "gray"])
plt.title("JJS Character Damage")
plt.xlabel("Character")
plt.ylabel("Damage")
plt.show()

# ==========================================
# 14 days, 14 clears. Phase 1 COMPLETE.
# ==========================================
