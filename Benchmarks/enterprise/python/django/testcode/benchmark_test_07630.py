# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from Crypto.Cipher import AES


def BenchmarkTest07630(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
