# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest45662(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    try:
        _bounded = int(data)
        if _bounded < 0 or _bounded > 10000:
            return JsonResponse({'error': 'out of range'}, status=400)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
