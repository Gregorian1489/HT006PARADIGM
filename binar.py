array = [1,2,3,5,7,10,20,35,49]
print(array)
search_num = int(input('Введите искомое число:\n'))

def binar_search(array, num, start = 0, end = None):
    start, end = 0, (len(array) - 1)
    while start <= end:
        mid = (start + end) // 2
        if num == array[mid]:
            return mid
        if num < array[mid]:
            end = mid - 1
        else:  
            start = mid + 1
    return -1

print ("Индекс искомого числа:")
print(binar_search(array, search_num))