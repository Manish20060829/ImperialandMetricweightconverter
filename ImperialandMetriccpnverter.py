def starting1():
    starting = input(
        "Welome to the metric and imperial weight converter do you want to play (yes or no): ").lower()
    if starting == "yes":
        numbers()
    if starting == 'no':
        exit()
    else:
        print("Not yes or no")
        starting1()


def numbers():
    try:
        global Number
        Number = int(input("Enter weight: "))
        if isinstance(Number, int):
            user()
    except ValueError:
        print('not a number')
        numbers()


def user():
    Choice = input(
        "What would you like to is your unit of measurement(Grams, Kilograms, Tonnes, Pounds, Us Tons, Ounces): ").lower()
    if Choice == "grams":
        grams()
    if Choice == "kilograms":
        kilograms()
    if Choice == "tonnes":
        tonnes()
    if Choice == "pounds":
        pounds()
    if Choice == "us tons":
        us_tons()
    if Choice == "ounces":
        ounces()
    else:
        print("Not a Unit")
        user()


def grams():
    gram = input(
        "What do you want to convert too(Kilograms, Tonnes, Pounds, Us Tons, Ounces): ").lower()
    if gram == 'kilograms':
        print(f'{float(Number / 1000)} in kilograms.')
        playing()
    if gram == 'tonnes':
        print(f'{float(Number / 1000000)} in tonnes.')
        playing()
    if gram == 'pounds':
        print(f'{float(Number / 453.59237)} in pounds.')
        playing()
    if gram == 'us tons':
        print(f'{float(Number / 907185)} in us tons.')
        playing()
    if gram == 'ounces':
        print(f'{float(Number / 28.35)} in ounces.')
        playing()
    else:
        print("Not a Unit")
        grams()


# note to self strings in if statement need to be lowers case


def kilograms():
    kilogram = input(
        "What do you want to convert too(Grams, Tonnes, Pounds, Us Tons, Ounces): ").lower()
    if kilogram == 'grams':
        print(f'{float(Number * 1000)} in grams.')
        playing()
    if kilogram == 'tonnes':
        print(f'{float(Number / 1000)} in tonnes.')
        playing()
    if kilogram == 'pounds':
        print(f'{float(Number * 2.20462)} in pounds.')
        playing()
    if kilogram == 'us tons':
        print(f'{float(Number / 907)} in us tons.')
        playing()
    if kilogram == 'ounces':
        print(f'{float(Number * 35.274)} in ounces.')
        playing()
    else:
        print("Not a Unit")
        kilograms()


def tonnes():
    tonne = input(
        "What do you want to convert too(Grams, Kilograms, Pounds, Us Tons, Ounces): ").lower()
    if tonne == 'grams':
        print(f'{float(Number * 1000000)} in grams.')
        playing()
    if tonne == 'kilograms':
        print(f'{float(Number * 1000)} in kilograms.')
        playing()
    if tonne == 'pounds':
        print(f'{float(Number * 2204.62)} in pounds.')
        playing()
    if tonne == 'us tons':
        print(f'{float(Number * 1.10231)} in us tons.')
        playing()
    if tonne == 'ounces':
        print(f'{float(Number * 35274)} in ounces.')
        playing()
    else:
        print("Not a Unit")
        tonnes()


def pounds():
    pound = input(
        "What do you want to convert too(Grams, Kilograms, Tonnes, Us Tons, Ounces): ").lower()
    if pound == 'grams':
        print(f'{float(Number * 453.592)} in grams.')
        playing()
    if pound == 'kilograms':
        print(f'{float(Number / 2.205)} in kilograms.')
        playing()
    if pound == 'tonnes':
        print(f'{float(Number / 2205)} in tonnes.')
        playing()
    if pound == 'us tons':
        print(f'{float(Number / 2000)} in us tons.')
        playing()
    if pound == 'ounces':
        print(f'{float(Number * 16)} in ounces.')
        playing()
    else:
        print("Not a Unit")
        pounds()


def us_tons():
    us_ton = input(
        "What do you want to convert too(Grams, Kilograms, Tonnes, Pounds, Ounces): ").lower()
    if us_ton == 'grams':
        print(f'{float(Number * 907185)} in grams.')
        playing()
    if us_ton == 'kilograms':
        print(f'{float(Number * 907.185)} in kilograms.')
        playing()
    if us_ton == 'tonnes':
        print(f'{float(Number / 1.10231)} in tonnes.')
        playing()
    if us_ton == 'pounds':
        print(f'{float(Number * 2000)} in pounds.')
        playing()
    if us_ton == 'ounces':
        print(f'{float(Number * 32000)} in ounces.')
        playing()
    else:
        print("Not a Unit")
        us_tons()


def ounces():
    ounce = input(
        "What do you want to convert too(Grams, Kilograms, Tonnes, Pounds, Us Tons): ").lower()
    if ounce == 'grams':
        print(f'{float(Number * 28.35)} in grams.')
        playing()
    if ounce == 'kilograms':
        print(f'{float(Number / 35.274)} in kilograms.')
        playing()
    if ounce == 'tonnes':
        print(f'{float(Number / 35274)} in tonnes.')
        playing()
    if ounce == 'pounds':
        print(f'{float(Number / 16)} in pounds.')
        playing()
    if ounce == 'us tons':
        print(f'{float(Number / 32000)} in us tons.')
        playing()
    else:
        print("Not a Unit")
        ounces()


def playing():
    Playing_again = input("Do you want to play again(yes or no): ").lower()
    if Playing_again == "yes":
        numbers()
    if Playing_again == "no":
        exit()
    else:
        print("Not yes or no")
        playing()


if __name__ == '__main__':
    starting1()
