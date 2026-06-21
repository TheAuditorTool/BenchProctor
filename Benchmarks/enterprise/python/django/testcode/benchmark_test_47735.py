# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47735(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
