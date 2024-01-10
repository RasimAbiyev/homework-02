# """
# Note. All tasks should be written as in the following example (you can
# use variable naming method or adding a comment after the expression):
# # A
expression = True and False or True
step_one = (True and False) or (True)
step_two = (False) or (True)
step_three = True
print(expression == step_three)

# At the end, your program should only print 'True's, so that will mean
# you have accomplished and simplified all expressions correctly.

# - Booleans -
# Simplify these expressions:
A = True or False and True
step_one = (True) or (False and True)
step_two = (True) or (False)
step_three = True
print(A == step_three)

B = False and False or False
step_one = (False and False) or (False)
step_two = (False) or (False)
step_three = False
print(B == step_three)

C = (True or False) and True
step_one = (True) and (True)
step_two = True
print(C == step_two)

D = True or (True or False and True) and True
step_one = (True) or (True or (False and True)) and (True)
step_two = (True) or (True or False) and (True)
step_three = (True) or (True) and (True)
step_four =  (True) or (True and True)
step_five = (True) or (True)
step_six = True
print(D == step_six)

E = False or False and False and not False
step_one = (False) and (False and False and not False)
step_two = (False) or (False and False and (not False))
step_three = (False) or (False and False and True)
step_four = (False) or ((False and False) and True)
step_five = (False) or (False and True)
step_six = (False) or (False)
step_seven = False
print(E == step_seven)

F = (True or True or False) and True
step_one = ((True or True) or False) and (True)
step_two = (True or False) and (True)
step_three = (True) and (True)
step_four = True
print(F == step_four)

G = False or (True and False)
step_one = (False) or (False)
step_two = False
print(G == step_two)

H = False and False and False and False and False or True and False
step_one = (False and False and False and False) or (True and False)
step_two = ((False and False) and False and False) or (False)
step_three = (False and False and False) or (False)
step_four = ((False and False) and False) or (False)
step_five = (False and False) or (False)
step_six = (False) or (False)
step_seven = False
print(H == step_seven)

I = True or False or True
step_one = (True or False) or (True)
step_two = (True) or (True)
step_three = True
print(step_three == I)

J = False or (not False)
step_one = (False) or (True)
step_two = True
print(J == J)

K = not True or not False
step_one = (not True) or (not False)
step_two = (False) or (True)
step_three = True
print(K == step_three)

L = False and not False or not False
step_one = (False) and (not False) or (not False)
step_two = (False) and (True) or (True)
step_three = (False and True) or (True)
step_four = (False) or (True)
step_five = True
print(L == step_five)

M = True or not False and True or not not True
step_one = (True) or (not False) and (True) or (not not True)
step_two = (True) or (True) and (True) or (not False)
step_three = (True) or (True and True) or (True)
step_four = (True) or (True) or (True)
step_five = (True or True) or (True)
step_six = (True) or (True)
step_seven = True
print(M == step_seven)

N = not not not False
step_one = (not not not False)
step_two = (not not(not False))
step_three = (not not True)
step_four = (not (not True))
step_five = (not False)
step_six = True
print(N == step_six)

# (previous task N's value) (N =  True)
O = not N
step_one = (not N)
step_two = (not True)
step_three = False
print (O == step_three)

P = True or False and not True or (not True and False) and not True or False
step_one = (True) or (False) and (not True) or ((not True) and False) and (not True) or (False)
step_two = (True) or (False) and (False) or (False and False) and (False) or (False)
step_three = (True) or (False and False) or (False) and (False) or (False)
step_four = (True) or (False) or (False and False) or (False)
step_five = (True) or (False) or (False) or (False)
step_six = ((True or False) or False or False)
step_seven = (True) or (False) or (False)
step_eight = ((True or False) or (False))
step_nine = (True) or (False)
step_ten = True
print(P == step_ten)

Q = True or not False or not True or True
step_one = (True) or (not False) or (not True) or (True)
step_two = (True) or (True) or (False) or (True)
step_three = ((True or True) or (False) or (True))
step_four = (True) or (False) or (True)
step_five = ((True or False) or (True))
step_six = (True) or (True)
step_seven = True
print(Q == step_seven)

R = False and (not True or False or (False or not True and True or False)) and True
step_one = (False) and ((not True) or (False) or ((False) or (not True) and (True) or (False))) and (True)
step_two = (False) and ((False) or (False) or ((False) or (False) and (True) or False)) and (True)
step_three = (False) and ((False) or (False) or ((False) or (False and True) or False)) and (True)
step_four = (False) and ((False) or (False) or ((False) or ((False) or (False)))) and (True)
step_five = (False) and ((False) or (False) or ((False or False or False))) and (True)
step_six = (False) and ((False) or (False) or (((False or False)) or (False))) and (True)
step_seven = (False) and ((False) or (False) or ((False) or (False))) and (True)
step_eight = (False) and ((False) or (False) or ((False or False))) and (True)
step_nine = (False) and ((False) or (False) or (False)) and (True)
step_ten = (False) and ((False or False or False)) and (True)
step_eleven = (False) and ((False or False) or (False)) and (True)
step_twelve = (False) and ((False) or (False)) and (True)
step_thirteen = (False) and ((False or False)) and (True)
step_fourteen = (False) and (False) and (True)
step_fifteen = (False and False and True)
step_sixteen = ((False and False) and (True))
step_seventeen = (False) and (True)
step_eighteen = False
print(R == step_eighteen)

S = False and not not not True and (False or True or not False) and True or False
step_one = (False) and (not not not True) and (False or True or not False) and (True or False)
step_two = (False) and (not not (not True)) and (False or True or (not False)) and (True)
step_three = (False) and (not not False) and (False or True or True) and (True)
step_four = (False) and (not (not False)) and ((False or True) or True) and (True)
step_five = (False) and (not True) and (True or True) and (True)
step_six = (False) and (False) and (True) and (True)
step_seven = (False and False) and (True) and (True)
step_eight = (False) and (True) and (True)
step_nine = (False and True) and (True)
step_ten = (False) and (True)
step_eleven = False
print(S == step_eleven)

T = not (True or False) or not False or (True and False or False)
step_one = not True or not False or (((True and False) or False))
step_two = (not True) or (not False) or (False or False)
step_three = (False) or (True) or (False)
step_four = (False or True) or (False)
step_five = (True) or (False)
step_six = True
print(step_six == T)

U = (True or not not False) and (True or (True or (False)))
step_one = ((True) or not (not False)) and (True or (True or False))
step_two = ((True) or not True) and (True or True)
step_three = ((True) or (not True) and (True))
step_four = (True or False) and (True)
step_five = (True) and (True)
step_six = True
print(U == step_six)

V = False and False or (not False and (not False))
step_one = (False and False) or ((not False) and (True))
step_two = (False) or (True and True)
step_three = (False) or (True)
step_six = True
print(V == step_six)

W = (not True or not False) and (not True or (not False))
step_one = ((not True) or (not False)) and (not True or True)
step_two = (False or True) and ((not True) or (True))
step_three = (True) and (False or True)
step_four = (True) and (True)
step_five = True
print(W == step_five)

X = False or False and not True or not False and (not True and False)
step_one = (False) or (False) and (not True) or (not False) and ((not True) or False)
step_two = (False) or (False) and (False) or (True) and (False or False)
step_three = (False) or (False and False) or (True) and (False)
step_four = (False) or (False) or (True and False)
step_five = (False) or (False) or (False)
step_six = ((False or False) or (False))
step_seven = (False) or (False)
step_eight = False
print(X == step_eight)

Y = True and True and True and True and not True and True and True or False
step_one = (True) and (True) and (True) and (not True) and (True) and (True) or (False)
step_two = (True) and (True) and (True) and (False) and (True) and (True) or (False)
step_three = (((True and True) and (True) and (False) and (True) and (True))) or (False)
step_four = ((True) and (True) and (False) and (True) and (True)) or (False)
step_five = (((True and True) and (False) and (True) and (True))) or (False)
step_six = ((True) and (False) and (True) and (True)) or (False)
step_seven = (((True and False) and (True) and (True))) or (False)
step_eight = ((False) and (True) and (True)) or (False)
step_nine =(((False and True) and (True))) or (False)
step_ten = ((False) and (True)) or (False)
step_eleven = ((False and True)) or (False)
step_twelve = (False) or (False)
step_eighteen = False
print(Y == step_eighteen)

Z = False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
step_one = (False) and (False) and (((True) or (not False) and ((True) or (False and True)))) or (not True) and (False) and ((not False) or (not True))
step_two = (False) and (False) and (((True) or (True) and ((True) or (False)))) or (False) and (False) and (True or False)
step_three = (False) and (False) and (((True) or (True) and (True or False))) or ((False and (False)) and (True))
step_four = (False) and (False) and (((True) or (True) and (True))) or ((False) and (True))
step_five = (False) and (False) and ((True) or (True and True)) or (False and True)
step_six = (False) and (False) and ((True) or (True)) or (False)
step_seven = (False) and (False) and ((True or True)) or (False)
step_eight = (False) and (False) and (True) or (False)
step_nine = ((False) and (False) and (True)) or (False)
step_ten = ((False and False) and (True)) or (False)
step_eleven = ((False) and (True)) or (False)
step_twelve = (False and True) or (False)
step_eighteen = (False) or (False)
step_fourteen = False
print(Z == step_fourteen)
# """