original_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {original_list}")

def filter_even_numbers(given_list):
    new_list = []
    for number in given_list:
        if number % 2 == 0: 
            new_list.append(number)
    return new_list
print(f"List with even numbers only: {filter_even_numbers(original_list)}")