# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42625(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
