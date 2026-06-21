# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import AES


def BenchmarkTest71786(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
