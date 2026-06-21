# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import AES


def relay_value(value):
    return value

def BenchmarkTest53698(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
