# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from Crypto.Cipher import DES


def BenchmarkTest10893(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
