#EKO Module

__version__ = 'Module v1.0 (create by M1sterEK0) date: 22.10.2019'



def Hi():
    '''Приветствие Братика'''

    print('Привет братик))')




def ArrayToCsvText(array):
    '''Преобразует 2-мерный массив в строку с переводом строки '\n' после каждого элемента массива\
    [[0, 1, 2, 3, 45],[10, 11, 12, 13, 14],[10, 11, 12, 13, 14],[30, 31, 32, 33, 34]]\
    Преобразует в:  0, 1, 2, 3, 45\n10, 11, 12, 13, 14\n10, 11, 12, 13, 14\n30, 31, 32, 33, 34'''
  
    
    return '\n'.join(','.join(map(str, line)) for line in array)
    #print('\n'.join(','.join(map(str, line)) for line in array))
