
def first_repeat(arr):
    count = {}
    for item in arr:
        if item in count:
            return item
        count[item] = 1
    return None

