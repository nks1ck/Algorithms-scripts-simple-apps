a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

def euclid_algorithm(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    print(first_number + second_number)

euclid_algorithm(a, b)
