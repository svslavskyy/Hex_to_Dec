import PySimpleGUI as sg


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

    return x


def math_f(S, p, m):
    E = abs(int(convert_base(p, from_base=2, to_base=10)))
    i = 0
    F = 0
    while i < len(m):
        F += 2 ** (-(i + 1)) * int(m[i])
        i += 1
    x = (-1) ** S * 2 ** (E - 1023) * (1 + F)
    return x


def converting_from_hex_to_decimal(hex):
    a = convert_base(hex, from_base=16, to_base=2)

    if (len(a) == 63):
        s = 0
        p = a[0:11]
        m = a[11:]
        return math_f(s, p, m)
    else:
        s = 1
        p = a[1:12]
        m = a[12:]
        return math_f(s, p, m)


def expand_hex(hex):
    hex_work = ""
    for i in range(int(len(hex) / 2)):
        hex_work += hex[-2 * (i + 1):len(hex) - 2 * i]
    return hex_work


def print_func():
    print(" HEX формат:                     ", hex, "    Обратный HEX формат:                       ", hex_expand)
    print()
    dec = converting_from_hex_to_decimal(hex)
    dec_expand = converting_from_hex_to_decimal((hex_expand))
    # dec_int = convert_base(hex, from_base=16, to_base=10)
    dec_int = int(str(hex), 16)
    dec_expand_int = int(str(hex_expand), 16)
    if abs(dec) > 9999999999:
        print("{b:25s}{a:25.10e}    ".format(a=dec, b=" DEC формат:"), end='')
    else:
        print("{b:25s}{a:25.14f}    ".format(a=dec, b=" DEC формат:"), end='')
    if abs(dec_expand) > 9999999999:
        print("{b:35s} {a:25.10e}    ".format(a=dec_expand, b=' Обратный DEC формат:'))
    else:
        print("{b:35s} {a:25.14f}    ".format(a=dec_expand, b=' Обратный DEC формат:'))

    print("{b:25s}{a:25.10e}    ".format(a=dec, b=' DEC в научном формате:'),
          "{b:35s}{a:25.10e}".format(a=dec_expand, b='Обратный DEC в научном формате: '))
    print("{b:25s}{a:25d}    ".format(a=dec_int, b=' DEC в int формате:'),
          "{b:35s}{a:25d}".format(a=dec_expand_int, b='Обратный DEC в int формате:'), "\n\n")


# 7C53 37E8 83F0 58E3
# A027AFDF5D984840
# C046FE93E4BD9E1F
# 0000 0000 0000 0000
# FFFF FFFF FFFF FFFF


layout = [
    [sg.Text('Число с плавающей точкой в HEX формате', font=('Helvetica', 16)), sg.InputText(''),],
    [sg.Output(size=(130, 30), key='-OUTPUT-', font=('Courier', 12))],
    [sg.Submit(), sg.Button('Clear'), sg.Button('FAQ')]
]

window = sg.Window('HEX to DEC', layout, resizable=True, element_justification="center").Finalize()
# window.Maximize()
while True:
    event, values = window.read()

    if event == 'FAQ':
        sg.popup('1) При невозможности вставить или скопировать текст - используйте английскую раскладку\n\n'
                 '2) Вводите Hex числа в формате 16 или 8 символов\n\n'
                 '3) При вводе числа в формате 8 символов, оставшиеся 8 будут дописаны нулями\n\n'
                 '4) Обратная запись при 8 символов происходит до момента добавление нулей', font=('Helvetica', 12))
        continue

    if event == 'Clear':
        window['-OUTPUT-'].update('')
        continue
    hex = values[0].replace(" ", "")
    hex = hex.upper()


    standart_hex = "ABCDEF0123456789"
    hex_to_work = ''
    error = False
    for x in hex:
        if (x in standart_hex):
            hex_to_work += x
        else:
            error = False
            break
        error = True
    stop_name = ['00000000', '0000000000000000', 'FFFFFFFF', 'FFFFFFFFFFFFFFFF']
    for x in stop_name:
        if hex == x:
            print('Введено граничное значение')
            error = False
            break
    if error == True:
        if len(hex) == 8:
            hex_expand = expand_hex(hex)
            hex_expand += "00000000"
            hex = hex + "00000000"
            print_func()
        elif len(hex) == 16:
            hex_expand = expand_hex(hex)
            print_func()
        else:
            print("Введите Hex число с 8 или 16 знаками")
    else:
        print("Веедите коректные данные")

    if event in (None, 'Exit'):
        break
