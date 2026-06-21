# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


request_state: dict[str, str] = {}

def BenchmarkTest19635(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
