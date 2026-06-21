# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60096(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
