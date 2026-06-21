# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35619(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
