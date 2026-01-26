number_list = [1,2,3,4,5]
def sum_of_list(given_list):
    list_sum = 0
    for number in given_list:
        list_sum += number
    return list_sum
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")