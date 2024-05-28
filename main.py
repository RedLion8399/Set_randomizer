# import PAckages
from random import randint as rd

# mainfunction
def main(names: list):
    # Print two random names from the lsit of names
    # delete the name from the list
    # repeat until the list is empty or only one person is left
    while len(names) > 1:
        name2 = names.pop(rd(0, len(names) - 1))
        name1 = names.pop(rd(0, len(names) - 1))
        print(f"{name1} : {name2}")
    if len(names) == 1:
        print(f"{names[0]} is left")

    return


# # Get List of names as user input
# names = input("Enter the list of names. Seperated by comma: ").split(",")
# # run main function with list of names
# main(names)


names = ["Mark", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Liam", "Mia", "Nick", "Olivia", "Paul", "Quinn", "Rachel", "Sam", "Toby", "Ursula", "Victor", "Wendy", "Xavier"]
main(names)