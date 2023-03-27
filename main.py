
import string


def rail_fence(input, n):
    i = 0
    lista = []
    is_up = False
    for j in range(0, n):
        lista.append('')
    for char in input:
        for j in range(0, n):
            if j == i:
                lista[j] = lista[j] + char
            else:
                lista[j] = lista[j] + ' '
        if i >= n-1:
            is_up = True
        elif i < 1:
            is_up = False
        if is_up:
            i = i - 1
        else:
            i = i + 1

    output = ''
    for eo in lista:
        output = output + eo.replace(' ', '')
    return output


def decript_rail_fence(input, n):
    matrix = []
    for i in range(n):
        matrix.append('')
    i = 0
    down = True
    for _ in input:
        for index, _ in enumerate(range(n)):
            if index == i:
                matrix[index] = matrix[index] + '-'
            else:
                matrix[index] = matrix[index] + ' '
        if down:
            i = i + 1
        else:
            i = i - 1
        if i == 0:
            down = True
        if i == n - 1:
            down = False
    i = 0
    for index1, string1 in enumerate(matrix):
        for char in string1:
            if char == '-':
                string1 = string1.replace('-', input[i], 1)
                i = i + 1
        matrix[index1] = string1
    i = 0
    j = 0
    down = True
    output = ''
    for index, _ in enumerate(input):
        output = output + matrix[i][index]
        if down:
            i = i + 1
        else:
            i = i - 1
        if i == 0:
            down = True
        if i == n - 1:
            down = False
    return output.replace(' ', '')


def matrix_a(input, key):
    matrix = []
    output = ''
    for index, _ in enumerate(key):
        matrix.append(input[0+index*4: 4+index*4])
    for string1 in matrix:
        for index in key:
            if not index > len(string1):
                output = output + string1[index-1]
    return output


def decript_matrix_a(input, key):
    tmp_matrix = []
    for index, _ in enumerate(key):
        tmp_matrix.append(input[0+index*len(key): 4+index*len(key)])
    matrix = []
    for _ in enumerate(key):
        matrix.append(' '*len(key))
    i = 0
    for tmp, out in zip(tmp_matrix, matrix):
        j = 0
        for x in key:
            if len(tmp) >= x:
                temp_string = list(out)
                temp_string[x - 1] = tmp[j]
                out = ''.join(temp_string)
                j = j + 1
        matrix[i] = out
        i = i + 1
    output = ''
    for x in matrix:
        output = output + x
    return output
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
