# uncompyle6 version 3.9.2
# Python bytecode version base 3.12.0 (3531)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: old_primes.py
# Compiled at: 2025-05-06 15:42:35
# Size of source mod 2**32: 295 bytes

import os
lower = 1
upper = 50
os.system('clear')
print('Numeros primeos entre %d y %d son: \n' % (lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)