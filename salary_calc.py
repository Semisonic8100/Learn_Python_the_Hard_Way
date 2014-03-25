#  Rough tool to gauge annual, monthly, and weekly take-home pay after taxes based on projected total tax burden.  
#  See http://usatoday30.usatoday.com/news/washington/tax-rates-spending.htm for a more comprehensive breakdown.

salary = float(raw_input('Enter Salary: '))
tax_burden = float(raw_input('Enter tax burden [Ex 25% = .25]: '))

salary = salary * (1 - tax_burden)  
annual = salary
monthly = salary / 12
weekly = salary / 52

print "Annual: $%r,\nMonthly $%r,\nWeekly $%r." % (annual, monthly, weekly)
