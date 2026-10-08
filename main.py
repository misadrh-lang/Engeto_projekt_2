import random
NUM_LENGTH = 4

def generate_secret_number() -> str:
    """Fce vygeneruje náhodné čtyřmístné číslo, kde první číslice nezačíná nulou."""
    secret_number = ""
    while len(secret_number) < NUM_LENGTH:
        digit = str(random.randint(0, 9))
        if len(secret_number) == 0 and digit == "0":
            continue
        if digit not in secret_number:
            secret_number += digit
    return secret_number
 

def get_valid_guess() -> str:
    """Fce vyžádá od uživatele tip na čtřmístné číslo, které splňuje pravidla hry."""
    while True:
        guess = input(">>> ")
            
        if not guess.isdigit():
            print("Wrong input, you have to enter a digit.")
            continue
        if len(guess) != NUM_LENGTH:
             print(f"Wrong input, the number has to have {NUM_LENGTH} digits.")
             continue
        if guess[0] == "0":
            print("Wrong input, number cannot start with 0.")
            continue
        if len(set(guess)) != NUM_LENGTH:
            print("Wrong input, number cannot use 2 same digits.")
            continue
        return guess

   
def evaluate_guess(secret_number: str, guess: str) -> tuple:
    """Fce porovnává náhodně vygenerované číslo a tip hráče a ukáže bulls a cows."""
    bulls = 0
    cows = 0
    for index in range(NUM_LENGTH):
        if guess[index] == secret_number[index]:
            bulls += 1
        elif guess[index] in secret_number:
            cows += 1
    return bulls, cows


def main() -> None:
    """Volá podfunkce a spoští celou hru bulls a cows."""
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = get_valid_guess()
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        bull_label = "bull" if bulls == 1 else "bulls"
        cow_label = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_label}, {cows} {cow_label}")
        print("-----------------------------------------------")

        if bulls == NUM_LENGTH:
            attempts_label = "guess" if attempts == 1 else "guesses"
            print("Correct, you've guessed the right number") 
            print(f"in {attempts} {attempts_label}!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
if __name__ == "__main__":
    main()
