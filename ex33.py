i = 0
numbers = []
x = int(raw_input("How much would you like to increment by?: "))

def loop_test(n):
    while n < 6:
        print "At the top i is %d" % n
        numbers.append(n)

        n += x
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % n

loop_test(i)

print "The numbers: "

for num in numbers:
    print num
