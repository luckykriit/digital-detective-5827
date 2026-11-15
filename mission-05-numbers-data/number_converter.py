
print("=== Number System Converter ===")
print("1. Decimal")
print("2. Binary")
print("3. Hexadecimal")

choice = input("Choose the input number system (1/2/3): ")
number = input("Enter the number: ")

try:
    if choice == "1":
        value = int(number, 10)
    elif choice == "2":
        value = int(number, 2)
    elif choice == "3":
        value = int(number, 16)
    else:
        print("Invalid choice")
        exit()

    print("Decimal:", value)
    print("Binary:", bin(value)[2:])
    print("Hexadecimal:", hex(value)[2:].upper())

except ValueError:
    print("Invalid number for the selected number system.")
