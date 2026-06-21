# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59719(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
