# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from Crypto.Cipher import DES


def to_text(value):
    return str(value).strip()

def BenchmarkTest29672(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
