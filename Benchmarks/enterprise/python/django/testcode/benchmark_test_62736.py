# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62736(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
