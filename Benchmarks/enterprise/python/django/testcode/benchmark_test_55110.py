# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55110(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ciphertext = bytes(b ^ 0x42 for b in str(origin_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
