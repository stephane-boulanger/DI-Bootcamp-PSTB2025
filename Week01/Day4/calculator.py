import operators_test

print(operators_test.ddOperator(5, 3))

print(operators_test.divideOperator(10, 2))

from operators_test import ddOperator

print(ddOperator(5, 3))

from operators_test import divideOperator as do

print(do(10, 2))
