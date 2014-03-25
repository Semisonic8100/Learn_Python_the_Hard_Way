def cats_and_kittens(cats, kittens):
    print "You have %d cats!" % cats
    print "You have %d kittens!" % kittens
    print "Man, that\'s enough for a Caturday!"
    print "Better get some cheeseburgers!\n"

print "We can just give the function numbers directly:"
cats_and_kittens(1, 2)

print "Or, we can use variables from our script:"    
fuzzy_butt = 1
random_kitten_name = 2
    
cats_and_kittens(fuzzy_butt, random_kitten_name)
    
print "We can even do math inside too:"
cats_and_kittens(2 + 5, 1 + 2)

print "And we can combine the two, variables and math:"
cats_and_kittens(fuzzy_butt * 5, random_kitten_name + 1)
