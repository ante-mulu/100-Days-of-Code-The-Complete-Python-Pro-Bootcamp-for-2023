import art
print(art.logo)
end = False
first_number = int(input("Enter the first Number"))
operation_input = input("Enter the operation. \n+\n-\n/\n*\n")
second_number = int(input("Enter the next number"))
while not end:
    def add():
        return first_number+second_number

    def sub():
        return first_number-second_number

    def mul():
        return first_number*second_number

    def div():
        return first_number/second_number

    def operation(op):
        switch = {
            '+': add(),
            '-': sub(),
            '*': mul(),
            '/': div(),
        }
        return switch.get(op, 'Choose one of the following operator:+,-,*,/,%')

    result = operation(op=operation_input)
    print(f"{first_number}{operation_input}{second_number}={result}")
    continue_new_option = input(
        "Type y to continue with the result n to start new calculation")
    if (continue_new_option == "y"):
        first_number = result
        operation_input = input("Enter the operation. \n+\n-\n/\n*\n")
        second_number = int(input("Enter the next number"))
    else:
        first_number = int(input("Enter the first Number"))
        operation_input = input("Enter the operation. \n+\n-\n/\n*\n")
        second_number = int(input("Enter the next number"))
