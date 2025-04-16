def main():
    while True:
        file_name = input("Type (input.txt): ")
        customers = read_file(file_name)

        if customers:
            while True:
                print("\nMenu:")
                print("1. Display transaction summary")
                print("2. Quit")

                choice = input("Pick 1 or 2: ")

                if choice == "1":
                    show_transaction_summary(customers)
                elif choice == "2":
                    print("Goodbye!")
                    return
                else:
                    print("Invalid option, try again.")
        else:
            if input("Invalid input. would you like to try again? (yes/no): ").lower() != "yes":
                print("Exiting.")
                break


def read_file(file_name):
    data = []
    try:
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, 1):
                parts = line.strip().split(",")
                if len(parts) != 4:
                    print(
                        f"[Line {line_num}] Incorrect format: {line.strip()}")
                    continue
                try:
                    amount = float(parts[3])
                    data.append([parts[0], parts[1], parts[2], amount])
                except ValueError:
                    print(
                        f"[Line {line_num}] Invalid number for amount: {parts[3]}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
    return data


def show_transaction_summary(customers):
    print("\nTransaction Summary")
    print("----------------------------------------------------------------------------")
    print("Transaction ID | First Name | Last Name | Before  | Discount  | After")
    print("----------------------------------------------------------------------------")
    for c in customers:
        before = c[3]
        discount = before * 0.40
        after = before - discount
        print(
            f"{c[0]:<15}| {c[1]:<10}| {c[2]:<10}| ${before:<8.2f}| ${discount:<9.2f}| ${after:.2f}")
    print("")


# Starts here
main()
