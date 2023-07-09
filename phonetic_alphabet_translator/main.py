import pandas

alphabet_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row["letter"]:row["code"] for (index, row) in alphabet_csv.iterrows()}

while True:
    user_input = input("Enter a word: ").upper()
    if user_input == "EXIT":
        break
    output = [alphabet[letter] for letter in list(user_input) if letter in alphabet.keys()]
    print(output)
