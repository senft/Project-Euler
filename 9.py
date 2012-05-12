LIMIT = 1000
ptrips = ((a, b, c) for a in xrange(LIMIT) for b in xrange(LIMIT) for c in
           xrange(LIMIT) if a ** 2 + b ** 2 == c ** 2
                         if a < b < c)
for trip in ptrips:
    a, b, c = trip
    if a + b + c == LIMIT:
        print a * b * c
        break
