secret_number = 13
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess :"))
    guess_count += 1
    if guess == secret_number:
        print("HURRYYY!! YOU WON")
        break
else :
    print("SORRY 'YOU LOOSE'")