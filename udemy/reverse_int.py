def reverse_int(num):
    num = str(num)
    reversed_int = num[::-1]
    return int(reversed_int)


def int_reversed(integer):
    integer = str(integer)
    # turning the integer into a list
    each_num = []
    for i in integer:
        each_num.append(i)

    # points to the first and the last element of the list
    index_one = 0
    index_final = len(integer)-1

    # cheking if they are the same

    while index_final > index_one:
        each_num[index_one], each_num[index_final] = each_num[index_final], each_num[index_one]
        index_one = index_one + 1
        index_final = index_final - 1
    return int(''.join(each_num))


def reverse_integer(value):
    reversed = 0
    remainder = 0
    while (value > 0):
        remainder = value % 10
        reversed = reversed * 10 + remainder
        value = value // 10
    return reversed


print(reverse_integer(1234))
print(int_reversed(1234))
print(reverse_int(1234))
