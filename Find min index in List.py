"""Write a function called max_index that, given a list of numbers, returns the index of the
largest value in the list. For example, given the list [40, 50, 10, 90, 100, 70], the function will
return 4"""
def max_index(numbers):
    if not numbers:
        return None
    return numbers.index(max(numbers))
num_list=[40, 50, 10, 90, 100, 70]
result=max_index(num_list)
print(result)