with open("./Input/Letters/starting_letter.txt") as file:
    template = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

for name in names:
    name_trimmed = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name_trimmed}.txt", "w") as file:
        file.write(template.replace("[name]", name_trimmed))
