#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org

def print_error():
    print('[!] invailed numeric string.')
    exit(1)

def input_filter():
    print('[*] You can input binary/decimal/hexadecimal numeric string to convert text.')
    data = raw_input('[<] ')
    if len(data) == 0:
        print_error()
    filter_char = []
    for num in xrange(0, 48):
        filter_char.append(chr(num))
    for num in xrange(58, 65):
        filter_char.append(chr(num))
    for num in xrange(71, 97):
        filter_char.append(chr(num))
    for num in xrange(103, 256):
        filter_char.append(chr(num))
    filter_char.append('0x', '0X', '0b', '0B')
    for char in filter_char:
        data = data.replace(char, '')

    return data


def input_detect(num_str):
    hexadecimal_feature = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
    for char in hexadecimal_feature:
        if char in num_str:
            print('[*] You may enter a hexadecimal numeric string.')
            return 16
    if max(num_str) == '1':
        print('[*] You may enter a binary numeric string.')
        return 2
    else:
        print('[*] You may enter a decimal numeric string.')
        return 10


def binary_to_text(num_str):
    lens = len(num_str)
    text = ''
    count = 0
    while count < lens:
        try:
            text += chr(int(num_str[:8], 2))
        except Exception as e:
            print_error()
        count += 8
        num_str = num_str[8:]
    print('[>] Output convert result:%s' %text)


def decimal_to_text(num_str):
    lens = len(num_str)
    text = ''
    count = 0
    while count < lens:
        if int(num_str[:2]) >= 32 and int(num_str[:2]) <= 126:
            text += chr(int(num_str[:2]))
            count += 2
            num_str = num_str[2:]
            continue
        elif int(num_str[:3]) >= 32 and int(num_str[:3]) <= 126:
            try:
                text += chr(int(num_str[:3]))
            except Exception as e:
                print_error()
            count += 3
            num_str = num_str[3:]
            continue
        else:
            print_error()
    print('[>] Output convert result:%s' %text)


def hexadecimal_to_text(num_str):
    lens = len(num_str)
    if lens % 2 != 0:
        print_error()
    try:
        text = num_str.decode('hex')
    except Exception as e:
        print_error()
    print('[>] Output convert result:%s' %text)


def main():
    num_str = input_filter()
    det_res = input_detect(num_str)
    if det_res == 2:
        binary_to_text(num_str)
    if det_res == 10:
        decimal_to_text(num_str)
    if det_res == 16:
        hexadecimal_to_text(num_str)
    

if __name__ == '__main__':
    main()
