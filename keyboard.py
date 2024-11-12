from typing import Optional

def str_to_float_two(a_str: str) -> Optional[float]:
    try:
        return str_to_float_two(a_str)
    except ValueError:
        return None
def gather_numbers():
    numbers = []

    while True:
        user_input = input("Enter a number, type done to end")
        if user_input == 'done':
            break

        number = str_to_float_two(user_input)
        if number is not None:
            numbers.append(number)
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print("collected numbers", numbers)
