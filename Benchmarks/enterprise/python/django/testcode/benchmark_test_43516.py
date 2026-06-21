# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43516(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ciphertext = bytes(b ^ 0x42 for b in str(auth_header).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
