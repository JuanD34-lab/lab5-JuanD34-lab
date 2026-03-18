from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response 

def main():
    seed = int(input("Enter a seed number: "))
    seed_secret_numbers(seed)

    secret = generate_secret_number()

    tries = 0
    guessed = False

    #Bucle del juego
    while not guessed:
        guess = int(input("what is your guess: "))
        tries += 1 
        message, guessed = input_response(secret, guess)
        print(message)

    print(f"It took you {tries} tries!")

if __name__ == "__main__":
    main()


