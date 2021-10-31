def multiply_self():
    results = 1
    end_character = 2
    print("This is my first project.\nThe given numbers will be multiplied until '0' is given as escape character")
    while end_character != 0:
        try:
            numbers_list = [int(input("Please enter a number: "))]
        except ValueError:
            print('\033[91m'+"Only numbers are allowed!"+'\033[0m')
        else:
            for input_be in numbers_list:
                results *= int(input_be)
            while True:
                try:
                    end_character = int(input("0=end, Any other number=continue: "))
                except ValueError:
                    print('\033[91m'+"Please follow the instructions strictly!"+'\033[0m')
                else:
                    break
    return results


end_result = multiply_self()
print(end_result)