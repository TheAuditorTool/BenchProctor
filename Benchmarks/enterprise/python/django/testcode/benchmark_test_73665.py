# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def BenchmarkTest73665(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
