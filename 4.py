def is_palindrom(x):
    return str(x) == str(x)[::-1]
largest = largest_i = largest_j = 0
for i in xrange(999):
    for j in xrange(999):
        product = i * j
        if product > largest and is_palindrom(product):
            largest = product
            largest_i = i
            largest_j = j
print largest_i, largest_j
