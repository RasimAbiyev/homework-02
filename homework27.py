expression = True and True
step_one = True
print(expression)

expression_one = False and True
step_one = False
print(expression_one)

expression_two = 1 == 1 and 2 == 1
step_one = True and False
step_two = False
print(expression_two)

expression_three = "test" == "test"
step_one = True
print(expression_three)

expression_four = 1 == 1 or 2 != 1
step_one = True or True
step_two = True
print(expression_four)

expression_five = True and 1 == 1
step_one = True and True
step_two = True
print(expression_five)

expression_six = False and 0 != 0
step_one = False and False
step_two = False
print(expression_six)

expression_seven = True or 1 == 1
step_one = True or True
step_two = True
print (expression_seven)

expression_eight = "test" == "testing"
step_one = False
print(expression_eight)

expression_nine = 1 != 0 and 2 == 1
step_one = True and False
step_two = False
print(expression_nine)

expression_ten = "test" != "testing"
step_one = True
print(expression_ten)

expression_eleven = "test" == 1
step_one = False
print(expression_eleven)

expression_twelve = not (True and False)
step_one = not False
step_two = True
print(expression_twelve)

expression_thirteen = not (1 == 1 and 0 != 1)
step_one = not (True and True)
step_two = not True
step_three = False
print(expression_thirteen)

expression_fourteen = not (10 == 1 or 1000 == 1000)
step_one = not (False or True)
step_two = not True
step_three = False
print(expression_fourteen)

expression_fifteen = not (1 != 10 or 3 == 4)
step_one = not (True or False)
step_two = not True
step_three = False
print(expression_fifteen)

expression_sixteen = not ("testing" == "testing" and "Zed" == "Cool Guy")
step_one = not (True and False)
step_two = not False
step_three = True
print(expression_sixteen)

expression_seventeen = 1 == 1 and (not ("testing" == 1 or 1 == 0))
step_one = True and (not (False or False))
step_two = True and (not False)
step_three = True and True
step_four = True
print(expression_seventeen)

expression_eighteen = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
step_one = True and (not (False or True))
step_two = True and(not True)
step_three = True and False
step_four = False
print(expression_eighteen)

expression_nineteen = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
step_one = True and (not (True or False))
step_two = True and (not True)
step_three = True and False
step_four = False
print(expression_nineteen)