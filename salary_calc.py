salary = int(raw_input('Enter Salary: '))

salary = salary * .75  ## Assumes 25% tax bracket
annual = salary
monthly = salary / 12
weekly = salary / 52

print "Annual: %r, Monthly %r, Weekly %r." % (annual, monthly, weekly)
