# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import AES


def BenchmarkTest11635(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
