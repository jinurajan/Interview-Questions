"""
Stay Positive

There is a given array of integers. Start with some value x and add each of the array elements to it consecutively. 
That is calculate a running sum of x plus each of the array elements.
Determine the minimum value of x such that the running sum is always atleast 1

Examples:

arr = [-4, 3, 2, 1]

if x == 5 running sums are

5 + -4 = 1
1 + 3 = 4
4 + 2 = 6
6 + 1 = 7
There is no smaller value for x  that satisfies the condition


arr = [3, -6, 5, 2, 1]

If the starting value is 4, running sums are [7,1,6,4,5]. This is the minimum starting value

"""


def minStartBF(arr):
    # idea is that to have the
    if not arr:
        return 0
    min_diff = arr[0]
    for i in range(len(arr)):
        if i == len(arr) - 1:
            break
        else:
            diff_sum = arr[i] + arr[i + 1]
            if diff_sum < min_diff:
                min_diff = diff_sum
    if min_diff >= 0:
        return 0
    min_val = 1 - min_diff

    # find the min in adding the consecutive elements
    # print "minimum value of x should be:{}".format(min_val)
    result = None
    for i in xrange(min_val, 100000000 + 1):
        x = i
        valid_for_all_array = False
        for each in arr:
            running_sum = x + each
            # print "{} + {} = {}".format(x, each, running_sum)
            if running_sum < 1:
                valid_for_all_array = False
                break
            else:
                valid_for_all_array = True
                x = running_sum
        if valid_for_all_array is True:
            result = i
            break
    return result


def minStart(arr):
    x = 0
    l = len(arr)
    if l == 0:
        return 1
    else:
        running_sum = 0
        min_value = 0
        for i in range(l):
            if arr[i] < min_value:
                min_value = arr[i]
            if running_sum + arr[i] > 0:
                running_sum = arr[i] + running_sum
            else:
                # some value is negative.we need to find the compliment value to meet the sum as 1
                # absolute value can be made by * -1 since arr[i] + running_sum is -1
                x = (arr[i] + running_sum) * -1 + 1 + x
                running_sum = 1
        if x == 0:
            # sum of array is 0
            # absolute value can be made  by x = (min(arr) + 1) * -1
            x = 1 - min_value + 1
        return x

if __name__ == '__main__':
    arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]  # -> 8 diffs are [-1, 2, 1, 4, 0, -7, -1, 5] -7+x = 1 -> x==8
    arr1 = [-5, 4, -2, 3, 1]  # -> diffs are [-1,2,1,4] -1+x = 1 x should be atleast 2
    arr2 = [3, -6, 5, -2, 1]  # -> 4 diffs are [-3, -1, 3, 1] -> -3+x = 1 x = 4
    arr3 = [-4, 3, 2, 1]  # -> diffs are [-1, 5, 3] -> -1+x = 1 x should be atleast 2
    arr4 = [-23457, -2374, 1, 23489, 19283]  # -> diffs are [-25831, -2375, 23490, 42772]
    arr5 = [234578, 34567, 789350]  # -> [269145,823917] if diff min is +ve return 1
    arr6 = [-237652, -141413, -141412]  # -> [-379065, -282825] -379065+x = 1 x -> 379066
    arr7 = [i if i % 3 == 0 else -i for i in xrange(100000)]
    print "minStart of {} is {}:".format(arr, minStart(arr))
    print "minStart of {} is {}:".format(arr1, minStart(arr1))
    print "minStart of {} is {}:".format(arr2, minStart(arr2))
    print "minStart of {} is {}:".format(arr3, minStart(arr3))
    print "minStart of {} is {}:".format(arr4, minStart(arr4))
    print "minStart of {} is {}:".format(arr4, minStart(arr5))
    print "minStart of {} is {}:".format(arr5, minStart(arr6))
    print "minStart of {} is {}:".format(arr6, minStart(arr7))
