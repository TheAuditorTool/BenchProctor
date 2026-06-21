# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

def BenchmarkTest68562(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
