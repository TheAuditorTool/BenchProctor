# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from Crypto.Cipher import DES


def BenchmarkTest32553(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
