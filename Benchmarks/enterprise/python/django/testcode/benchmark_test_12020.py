# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

def BenchmarkTest12020(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
