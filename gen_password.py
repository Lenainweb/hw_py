#!/usr/bin/env python3

from os import path
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


MIN_LEN_PWD = 4
LEN_PWD = 12
LONG_PDW = 128
MAX_LEN_PWD = 1000000

FILE_NAME = "password.txt"
FILE_PATH = "./"

interaction_str = dict(
    welcome="Welcome to the Linux User Password Generator!\n",
    prompt_len_pwd=f"Please enter the desired password length"
    f"(skip to generate password with default length {LEN_PWD}): ",
    prompt_save_in_file="Do you want to save the password to a file? (N/y): ",
    prompt_path="Enter the path to the file (skip to save in current directory) ",
    prompt_filename=f"Enter the desired filename (skip to save with default name '{FILE_NAME}') ",
    refine_filename="Such a file already exists. Overwrite? (N/y): ",
    result="\nGenerated password: ",
    length_error=f"Enter an integer, minimum password length: {MIN_LEN_PWD},"
    f" maximum password length: {MAX_LEN_PWD}",
    refine_len=f"The password is longer than {LONG_PDW} characters. "
    "Are you sure you want a password of the given length? (N/y): ",
    pwd_saved_to_file="\nPassword saved to file: ",
    access_error="No permission to write the file at the given address.",
    not_found_error="Specified address not found.",
    hint_yes_no="Please enter 'Y' (yes) or 'N' (no).",
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


def gen_pwd(length: int = MIN_LEN_PWD) -> str:
    """
    Generate a random password consisting of a
    combination of uppercase letters, lowercase letters,
    numbers, and special characters.
    """
    characters = ascii_lowercase + ascii_uppercase + digits + punctuation
    pwd = "".join(choices(characters, k=length))

    if check_strict(pwd):
        return pwd

    return gen_pwd(length=length)


def write_file(filename: str, data: str) -> str:
    """Write password to file."""

    with open(filename, "w") as file:
        file.write(data)

    return filename


def get_pwd_len() -> int:
    """
    Get the desired password length from the user,
    check if the length matches the given restrictions.
    """
    length = input(interaction_str["prompt_len_pwd"]).replace(",", ".")

    if not length:
        return LEN_PWD
    else:
        try:
            length = float(length)
            if not length % 1 == 0:
                print(interaction_str["length_error"])
                return get_pwd_len()

            length = int(length)
        except UnicodeDecodeError:
            print("I am decoding error. Then someday they'll fix me. Try again.")
            return get_pwd_len()
        except ValueError:
            print(interaction_str["length_error"])
            return get_pwd_len()

    if MIN_LEN_PWD <= length <= MAX_LEN_PWD:
        if length > LONG_PDW:
            while True:
                confirmation = input(interaction_str["refine_len"])
                if not confirmation or confirmation.lower() == "n":
                    return get_pwd_len()
                elif confirmation.lower() == "y":
                    break
                print(interaction_str["hint_yes_no"])
        return length

    print(interaction_str["length_error"])
    return get_pwd_len()


def save_pwd_to_file(pwd: str) -> None:
    """
    Get the file name and path from the user, write the password there.
    """
    home = path.expanduser("~")
    file_path = (
        input(interaction_str["prompt_path"])
        .replace("~", home)
        .replace("$(HOME)", home)
        .replace("$HOME", home)
        or FILE_PATH
    )
    file_name = input(interaction_str["prompt_filename"]) or FILE_NAME
    path_name_file = path.join(file_path, file_name)

    if path.isfile(path_name_file):
        while True:
            confirmation = input(interaction_str["refine_filename"])
            if not confirmation or confirmation.lower() == "n":
                return save_pwd_to_file(pwd)
            elif confirmation.lower() != "y":
                print(interaction_str["hint_yes_no"])
                continue
            break
    try:
        file = write_file(path_name_file, pwd)
        print(interaction_str["pwd_saved_to_file"], file)
        return None
    except (FileNotFoundError, NotADirectoryError):
        print(interaction_str["not_found_error"])
        return save_pwd_to_file(pwd)
    except PermissionError:
        print(interaction_str["access_error"])
        return save_pwd_to_file(pwd)


def generate_password() -> None:
    """
    Prompt the user to enter the desired length for the password.
    Generate a random password consisting of a combination of uppercase
    letters, lowercase letters, numbers, and special characters.
    Saves the password to a file. Display the generated password to the user.
    """
    print(interaction_str["welcome"])
    length = get_pwd_len()
    pwd = gen_pwd(length)

    while True:
        save_to_file = input(interaction_str["prompt_save_in_file"])

        if save_to_file and save_to_file.lower() == "y":
            save_pwd_to_file(pwd)
        elif save_to_file and save_to_file.lower() != "n":
            print(interaction_str["hint_yes_no"])
            continue
        break

    print(interaction_str["result"], pwd)


if __name__ == "__main__":
    generate_password()
