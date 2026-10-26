
def clean_number(text):
    return text.strip().replace(" ", "").replace("-", "")


def is_valid(number):
    return len(number) == 10 and number.isdigit() and number.startswith("0")


def digit_sum(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total


def main():
    phone = input("Phone number: ")

    number = clean_number(phone)

    if not is_valid(number):
        print("Invalid phone number")
        return

    formatted = number[:3] + "-" + number[3:6] + "-" + number[6:]
    hidden = number[:3] + "-XXX-" + number[6:]

    print("Formatted:", formatted)
    print("Hidden:", hidden)
    print("Digit sum:", digit_sum(number))


if __name__ == "__main__":
    main()