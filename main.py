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
        if i >= n - 1:
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
    length = round((len(input) / len(key)) + 0.5)
    for index, _ in enumerate(range(length)):
        matrix.append(input[0 + index * len(key): len(key) + index * len(key)])
    for string1 in matrix:
        for index in key:
            if not index > len(string1):
                output = output + string1[index - 1]
    return output


def decript_matrix_a(input, key):
    tmp_matrix = []
    length = round(((len(input) / len(key)) + 0.5))
    for index, _ in enumerate(range(length)):
        tmp_matrix.append(input[0 + index * len(key): len(key) + index * len(key)])
    matrix = []
    for _ in enumerate(range(length)):
        matrix.append(' ' * len(key))
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


def matrix_b(input, key):
    input = input.replace(' ', '')
    length = 0
    matrix = []
    i = 0
    while length < len(input):
        matrix.append(input[0 + (len(key)) * i: len(key) + (len(key)) * i])
        i = i + 1
        length = length + len(key)
    matrix[len(matrix) - 1] = matrix[len(matrix) - 1]
    key_order = [0 for _ in key]
    i = 1
    for letter in string.ascii_uppercase:
        for index, x in enumerate(key):
            if letter == x:
                key_order[index] = i
                i = i + 1
    i = 1
    output = ''
    for _ in key_order:
        for index, x in enumerate(key_order):
            if x == i:
                for line in matrix:
                    try:
                        output = output + line[index]
                    except:
                        pass
                output = output + ' '
                i = i + 1
    return output


def matrix_c(input, key):
    input = input.replace(' ', '')
    key_order = [0 for _ in key]
    i = 1
    for letter in string.ascii_uppercase:
        for index, x in enumerate(key):
            if letter == x:
                key_order[index] = i
                i = i + 1
    lenght = 0
    matrix = []
    i = 1
    while lenght < len(input):
        for index, x in enumerate(key_order):
            if x == i:
                insert_to = index + 1
                break
        i = i + 1
        start = lenght
        finish = lenght + insert_to
        matrix.append(input[start:finish])
        lenght = lenght + insert_to
    i = 1
    output = ''
    for _ in key_order:
        for index, x in enumerate(key_order):
            if x == i:
                for line in matrix:
                    try:
                        output = output + line[index]
                    except:
                        pass
                output = output + ' '
                i = i + 1
    print(output)
    return output


def cezar(input, n):
    output = ''
    for x in input:
        s = chr(ord(x) + n)
        output = output + str(s)
    return output


def decript_cezar(input, n):
    output = ''
    for x in input:
        s = chr(ord(x) - n)
        output = output + str(s)
    return output


def vigenere(input, key):
    output = ''
    for input_char, key_char in zip(input, key):
        x = ord(input_char) + ord(key_char)
        if x > 155:
            x = x - 26
        output = output + str(chr(x - 65))
    return output


def decript_vigenere(input, key):
    output = ''
    matrix = []
    tmp = ''
    for x in range(65, 91):
        tmp = ''
        for y in range(65, 91):
            if (x + y) > 155:
                tmp = tmp + chr(x + y - 26 - 65)
            else:
                tmp = tmp + chr(x + y - 65)
        matrix.append(tmp)
    for input_char, key_char in zip(input, key):
        x = ord(key_char) - 65
        tmp_string = matrix[x]
        output = output + str(chr(tmp_string.index(input_char) + 65))
    return output


def tests(text):
    # Rail Fence
    crypted = rail_fence(text, 5)
    assert text == decript_rail_fence(crypted, 5)
    crypted = rail_fence(text, 2)
    assert text == decript_rail_fence(crypted, 2)
    # Matrix_A
    crypted = matrix_a(text, (2, 3, 1, 4))
    assert text == decript_matrix_a(crypted, (2, 3, 1, 4))
    crypted = matrix_a(text, (2, 3, 1, 4, 6, 5))
    assert text == decript_matrix_a(crypted, (2, 3, 1, 4, 6, 5))
    # Cezar
    crypted = cezar(text, 5)
    assert text == decript_cezar(crypted, 5)
    crypted = cezar(text, 2)
    assert text == decript_cezar(crypted, 2)
    # Vigenere
    crypted = vigenere(text, 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
    assert text == decript_vigenere(crypted, 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
    crypted = vigenere(text, 'ACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBD')
    assert text == decript_vigenere(crypted, 'ACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBD')


if __name__ == '__main__':
    tests('CRYPTOGRAPHYCRYPTOGRAPHYCRYPTOGRAPHYCRYPTOGRAPHY')
    end = True
    while end:
        print("""
        1.Rail Fence,
        2.Matrix_A
        3.Matrix_B
        4.Matrix_C
        5.Cezar
        6.Vigenere
        7.Exit
        """)
        x = input()
        if int(x) == 1:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key: ')
            if x == '1':
                print(rail_fence(text, int(key)))
            elif x == '2':
                print(decript_rail_fence(text, int(key)))
        elif int(x) == 2:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key(with - in between): ')
            key_list = [int(x) for x in key.split('-')]
            if x == '1':
                print(matrix_a(text, key_list))
            elif x == '2':
                print(decript_matrix_a(text, key_list))
        elif int(x) == 3:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key(with - in between): ')
            key_list = [int(x) for x in key.split('-')]
            if x == '1':
                print(matrix_b(text, key_list))
            elif x == '2':
                pass
        elif int(x) == 4:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key(with - in between): ')
            key_list = [int(x) for x in key.split('-')]
            if x == '1':
                print(matrix_c(text, key_list))
            elif x == '2':
                pass
        elif int(x) == 5:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key: ')
            if x == '1':
                print(cezar(text, int(key)))
            elif x == '2':
                print(decript_cezar(text, int(key)))
        elif int(x) == 6:
            print("""
            1.Encript
            2.Decript
            """)
            x = input()
            text = input('Text: ')
            key = input('key: ')
            if x == '1':
                print(vigenere(text, key))
            elif x == '2':
                print(decript_vigenere(text, key))
        elif int(x) == 7:
            end = False

