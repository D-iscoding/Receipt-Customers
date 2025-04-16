def main():
    while True:
        file_name = input("Type - input.txt: ")
        customers = read_file(file_name)

        if not customers:
            try_again = input("File not found, would you like to try again? (yes/no): ")
            if try_again != "yes":
                print("FareWell!")
                break
            continue

        while True:
            print("")
            print("Menu:")
            print("1. Show transaction ID and names")
            print("2. Show full receipt")
            print("3. Quit")

            choice = input("Pick 1, 2 or 3: ")

            if choice == "1":
                show_ids_and_names(customers)
            elif choice == "2":
                show_receipt(customers)
            elif choice == "3":
                print("The End!")
                return
            else:
                print("Invalid option")

            again = input("Would you like to see the menu again? (yes/no): ")
            if again != "yes":
                print("FareWell")
                return


def read_file(file_name):
    records = []
    try:
        file = open(file_name, "r")
        for line in file:
            line = line.strip()
            parts = line.split(",")
            if len(parts) == 4:
                transaction_id = parts[0]
                first = parts[1]
                last = parts[2]
                try:
                    amount = float(parts[3])
                    record = (transaction_id, first, last, amount)
                    records.append(record)
                except:
                    print("One of the amounts wasn't a number.")
            else:
                print("One of the lines is not in the right format.")
        file.close()
    except:
        print("Could not open the file.")
    return records


def show_ids_and_names(customers):
    print("")
    print("Transaction ID and Names")
    print("-----------------------------")
    for customer in customers:
        transaction_id = customer[0]
        first = customer[1]
        last = customer[2]
        print("ID:", transaction_id, "|", first, last)
    print("")


def show_receipt(customers):
    print("")
    print("Full Receipt")
    print("----------------------------------------------")
    for customer in customers:
        first = customer[1]
        last = customer[2]
        amount = customer[3]
        discount = amount * 0.4
        total = amount - discount

        print("Name:", first, last)
        print("Before: $", round(amount, 2))
        print("Discount: $", round(discount, 2))
        print("After: $", round(total, 2))
        print("----------------------------------------------")
    print("")


main()
