#!/usr/bin/env python3

from time import time_ns
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


MIN_LEN_PWD = 6
LEN_FOR_FILE_PWD = 128

interaction_str = dict(
    welcome="Welcome to the Linux User Password Generator!\n",
    prompt=f"Please enter the desired password length (skip to generate password with default length {MIN_LEN_PWD}): ",
    result="\nGenerated password: ",
    length_error=f"Enter an integer, minimum password length: {MIN_LEN_PWD}",
    refine_len=f"The password is longer than {LEN_FOR_FILE_PWD} characters. "
    "Are you sure you want a password of the given length (the password will be saved in a file)? (N/y): ",
    pwd_saved_to_file="Password saved to file",
)


def check_strict(pwd: str) -> bool:
    """
    Check password to contains at least one uppercase letter,
    lowercase letter, number, special character.
    """
    return not (
        set(ascii_lowercase).isdisjoint(pwd)
        or set(ascii_uppercase).isdisjoint(pwd)
        or set(digits).isdisjoint(pwd)
        or set(punctuation).isdisjoint(pwd)
    )


def _gen_pwd(length: int = MIN_LEN_PWD) -> str:
    """
    Generate a random password consisting of a
    combination of uppercase letters, lowercase letters,
    numbers, and special characters.
    """
    characters = ascii_lowercase + ascii_uppercase + digits + punctuation
    pwd = "".join(choices(characters, k=length))

    if check_strict(pwd):
        return pwd

    return _gen_pwd(length=length)


def save_pwd_to_file(pwd: str) -> str:
    """Write password to file."""

    filename = "password_" + str(time_ns()) + ".txt"
    with open(filename, "w") as file:
        file.write(pwd)

    return filename


def generate_password() -> None:
    """
    Prompt the user to enter the desired length for the password.
    Generate a random password consisting of a combination of uppercase
    letters, lowercase letters, numbers, and special characters.
    Display the generated password to the user.
    """
    print(interaction_str["welcome"])

    while True:
        length = input(interaction_str["prompt"])

        if not length:
            length = MIN_LEN_PWD
        else:
            try:
                length = int(length)
            except ValueError:
                print(interaction_str["length_error"])
                continue

        if length < MIN_LEN_PWD:
            print(interaction_str["length_error"])
            continue

        if length > LEN_FOR_FILE_PWD:
            confirmation = input(interaction_str["refine_len"])

            if confirmation.lower() == "y":
                pwd = _gen_pwd(length)
                filename = save_pwd_to_file(pwd)
                print(interaction_str["pwd_saved_to_file"], filename)
                break
            continue

        else:
            pwd = _gen_pwd(length)
            print(interaction_str["result"], pwd)
            break


if __name__ == "__main__":
    generate_password()
