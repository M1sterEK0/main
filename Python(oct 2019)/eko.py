#EKO Module

'''Hi()-Приветствие;
   ArrayToCsvText(array) - Преобразование 2-мерного массива в CSV(str)
   DeleteDigits(string) - Удаление цифр из строки. Оставляет только буквы.'''


__version__ = 'Module v1.0 (create by M1sterEK0) date: 22.10.2019'



def Hi():
	'''Приветствие Братика'''

	print('Привет братик))')




def ArrayToCsvText(array):
	'''Преобразует 2-мерный массив в строку с переводом строки '\n' после каждого элемента массива\
	[[0, 1, 2, 3, 45],[10, 11, 12, 13, 14],[10, 11, 12, 13, 14],[30, 31, 32, 33, 34]]\
	Преобразует в:  0, 1, 2, 3, 45\n10, 11, 12, 13, 14\n10, 11, 12, 13, 14\n30, 31, 32, 33, 34'''
  
	#print('\n'.join(','.join(map(str, line)) for line in array))
	return '\n'.join(','.join(map(str, line)) for line in array)
    


def DeleteDigits(string):
	'''Преобразование строки, путем удаления цифр из этой строки. Оставляет только буквы.'''
	
	#print(''.join(x for x in a if not x.isdigit()))
	return ''.join(x for x in string if not x.isdigit())
	
