# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59322(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
