# noinspection PyUnresolvedReferences
'''
test program
'''
import matrtools as mt
print(' Метод Гаусса')
matr_a = [[2,4], [3,5], [6,7]]
#matr_a = mt.zapoln_matr()
mt.print_matrix(matr_a)
print('test1')


a_gauss = mt.echelon_form(matr_a)
mt.print_matrix(a_gauss)





