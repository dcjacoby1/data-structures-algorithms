string = "Hello"
reverse_string = ""
def reverse_string(str):
    reverse_str = ""
    for letter in str:
        reverse_str = letter + reverse_str
    return reverse_str



#wrong way i tried to do it
# def merged_array(arr_1, arr_2):
#     for i in arr_2:
#         if arr_2[i] >= arr_1[len[arr_1] -1]:
#                 arr_1.append[arr_2[i]]
#         else:
#             for j in arr_1:
#                 if arr_2[i] <= arr_1[j]:
#                     arr_1.insert(j, arr_2[j])
#                     break
                
            
#correct version for making a sorted merged array, using 2 sorted arrays
def merged_array(arr_1, arr_2):
    # Temporary list to store the merged result
    merged = []

    # Pointers for arr_1 and arr_2
    i = 0
    j = 0

    # Merge arr_1 and arr_2
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            merged.append(arr_1[i])
            i += 1
        else:
            merged.append(arr_2[j])
            j += 1

    # Append remaining elements of arr_1
    while i < len(arr_1):
        merged.append(arr_1[i])
        i += 1

    # Append remaining elements of arr_2
    while j < len(arr_2):
        merged.append(arr_2[j])
        j += 1
