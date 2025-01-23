from datetime import datetime
rent = 8000
groceries=41
total = rent + groceries
print(total) # 8041
# True= 7 ---- Cannot assigned to reserved key words
# foo+bar=5 ---- cannot assigned to operator
# 4you = 4 --- Syntax error: invalid syntax
# $error=404 --- Syntax error: invalid syntax
# error%$error=501 --- Syntax error: invalid syntax
foo=5
bar='jalebi'
foo=bar
bar=foo
id(foo)
id(bar)


# Assuming dob and todaydate are strings in the format dd/mm/yyyy
dob = datetime.strptime('23/05/1994', '%d/%m/%Y')
todaydate = datetime.strptime('01/05/2024', '%d/%m/%Y')

# Calculating age
age = todaydate.year - dob.year - ((todaydate.month, todaydate.day) < (dob.month, dob.day))

print(age)