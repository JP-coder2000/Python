array = [12,6,2,1,9,10,3]

def reverse_array(array):
    #pointing to the first item of the list
    start_index = 0
    #pointing to the last item of the list
    end_index = len(array)-1

    while end_index > start_index:
        #this is where we swap, we change each value with it's respective index
        array[start_index], array[end_index] = array[end_index], array[start_index]
        #we increment/decrement the value so that eventually our loop will end
        start_index = start_index + 1
        end_index = end_index - 1



reverse_array(array)
print(array)