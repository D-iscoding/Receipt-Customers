def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        return data


def menu():
    print("Menu")
    print(" 1 - Transaction IDs and usernames")
    print(" 2 - Total beofre and after discount")
    print(" 3 - quit")


def choice_1():
    print("")
    for transaction_id, f_name, l_name in zip(ids, first_name, last_name):
        print(transaction_id, f_name + l_name)


def choice_2():
    for f_name, l_name, before_ammount, after_ammount, saved_ammount in zip(first_name, last_name, before, after, saved):
        print(f_name + l_name, before_ammount, after_ammount, saved_ammount)


def choice_3():
    print("The End!")


# main starts here
data = read_file("data.txt")
ids = []
first_name = []
last_name = []
before = []
after = []
saved = []
for line in data[1:]:
    line_data = line.strip().split()
    ids.append(line_data[0])
    first_name.append(line_data[1])
    last_name.append(line_data[2])
    before.append(float(line_data[3]))
    after.append(float(line_data[4]))
    saved.append(float(line_data[5]))

print("IDs", ids)
print("First Names", first_name)
print("Last Names", last_name)
print("Before", before)
print("After", after)
print("Saved", saved)

menu()

choice = input("Enter your choice (1, 2, or 3): ")
if choice == "1":
    choice_1()
elif choice == "2":
    choice_2()
elif choice_3 == "3":
    choice_3()
