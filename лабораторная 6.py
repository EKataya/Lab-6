#подключаем numpy
import numpy as np
cr_amount = int(input("Введите количество критериев: "))

i = 1
#создаем  матрицу
matr = np.eye(cr_amount)
# цикл для заполнения матрицы
for q in range(i, cr_amount+1):
  for p in range(i+1, cr_amount+1):
    matr[q-1][p-1] = round(float(input("Введите отношение  критериев {0}-{1}: ".format(q, p))), 3)
    matr[p-1][q-1] = round((matr[q-1][p-1])**(-1), 2)
  i += 1
# создаем  список весовых коэффициентов
sum_matr = [round(sum(j),2) for j in matr]
# выводим список коэффициентов
print('Весовые коэффициенты:')
for k in sum_matr:
  print(round(k/sum(sum_matr), 2), end=' ')

