"""
Password Generator 
A mini Python project using the `random` module.
"""

import random
import string

rng = random.SystemRandom()

def generate_password(lenght=12, use_upper=True, use_digits=True, use_symbols=True):
    """Build a random password that includes at least one char of each chosen type."""
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("#$@%!^&*()><<>?/':;,.""")

    if lenght < len(pools):
        raise ValueError(f"Lenght must be at least {len(pools)}")

    # Guarantee one character from each selected pool
    password = [rng.choice(pool) for pool in pools]

    # Fill the rest from all pools combined
    all_chars = "".join(pools)
    password += [rng.choice(all_chars) for _ in range(lenght - len(password))]

    # Shuffle so the guaranteed characters aren't always at the start
    rng.shuffle(password)
    return "".join(password)

def strenght(password):
    """Very simple strength rating based on length and variety."""
    veriety = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ])
    score = veriety + (len(password) >= 12) + (len(password) >= 16)
    return ["Weak", "Weak", "Fair", "Good", "Strong", "Very Strong", "Very Strong"][score]

def ask_yes_no(question):
    return input(f"{question} (y/n): ").strip().lower().startswith("y")

def main():
    print("="*35)
    print("WELCOME TO THE PASSWORD GENERATOR")
    print("="*35)
    print("This program will generate a random password for you.")
    while True:
        try:
            length = int(input("\nPassword length: "))
            count = int(input("How many passwords? "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
 
        use_upper = ask_yes_no("Include uppercase letters?")
        use_digits = ask_yes_no("Include numbers?")
        use_symbols = ask_yes_no("Include symbols?")
        try:
             print("\nYour passwords:")
             for _ in range(count):
                pwd = generate_password(length, use_upper, use_digits, use_symbols)
                print(f"{pwd}  ({strenght(pwd)})")
        except ValueError as e:
            print(e)
            continue
        if not ask_yes_no("\nGenerate more passwords?"):
            break


if __name__ == "__main__":
    main()
