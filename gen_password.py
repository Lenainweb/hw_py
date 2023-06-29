from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


MIN_LEN_PWD = 6

interaction_str = dict(
    welcome="Welcome to the Linux User Password Generator!\n",
    prompt="Please enter the desired password length: ",
    result="\nGenerated password: ",
    length_error=f"Enter a number of minimum length: {MIN_LEN_PWD}",
)

characters = ascii_lowercase + ascii_uppercase + digits + punctuation


def check_strict(pwd: str) -> bool:
    """
    Check password to contains at least one uppercase letter,
    lowercase letter, number, special character.
    """
    if (
        set(ascii_lowercase).isdisjoint(pwd)
        or set(ascii_uppercase).isdisjoint(pwd)
        or set(digits).isdisjoint(pwd)
        or set(punctuation).isdisjoint(pwd)
    ):
        return False
    return True


def _gen_pwd(length: int) -> str:
    """
    Generate a random password consisting of a
    combination of uppercase letters, lowercase letters,
    numbers, and special characters.
    """
    result = [choice(characters) for i in range(length)]
    return "".join(result)


def gen_pwd() -> None:
    """
    Prompt the user to enter the desired length for the password.
    Generate a random password consisting of a combination of uppercase
    letters, lowercase letters, numbers, and special characters.
    Display the generated password to the user.
    """
    print(interaction_str["welcome"])

    try:
        length = int(input(interaction_str["prompt"]))
    except ValueError as e:
        print(interaction_str["length_error"])
        exit(2)

    if length < MIN_LEN_PWD:
        print(interaction_str["length_error"])
        exit(2)

    pwd = _gen_pwd(length)

    while not check_strict(pwd):
        pwd = _gen_pwd(length)

    print(interaction_str["result"], pwd)


if __name__ == "__main__":
    gen_pwd()
