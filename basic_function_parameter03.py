# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest():
    a=[1,2,3,4,5,6,7,8,9]
    min=a[0]
    for i in a:
        if i<min:
            min=i
    return min
print(find_smallest())
