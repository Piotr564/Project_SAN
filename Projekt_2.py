def switch_case(option):
    switch = {
        'a': "Kebab",
        'b': "Paruwa",
        'c': "Flaczki"
    }
    return switch.get(option, "Invalid option")

names = ['Mietek', 'Marek', 'Darek']
upper_names = list(map(str.upper, names))

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)

option = input("Choose an option ('a', 'b', or 'c'): ")
result = switch_case(option)

print("Original names:", names)
print("Names in upper case:", upper_names)
print("Original numbers with duplicates:", numbers)
print("Unique numbers:", unique_numbers)
print("Switch case result:", result)
