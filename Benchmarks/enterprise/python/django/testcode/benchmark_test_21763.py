# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.Cipher import DES
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

def BenchmarkTest21763(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
