# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03613(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
