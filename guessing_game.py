secret_num = 6
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Enter Guess :"))
    guess_count += 1
    if guess == secret_num:
        print("You won")
        break
else:
    print("Try again")