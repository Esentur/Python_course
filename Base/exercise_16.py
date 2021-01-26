from exercise_module import *
from random import *

array = [int(random() * 10) for i in range(0, 3)]
print(array)
print('Максимально значение в списке:', getMax(array))
print('Минимальное значение в списке:', getMin(array))
print('Сумма значений элементов в списке:', getSum(array))
