# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.Cipher import AES


def BenchmarkTest20475(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(graphql_var).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
