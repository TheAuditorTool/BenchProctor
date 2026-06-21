# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from Crypto.Cipher import DES


request_state: dict[str, str] = {}

def BenchmarkTest42357(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
