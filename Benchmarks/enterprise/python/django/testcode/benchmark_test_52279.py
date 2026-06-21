# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52279(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ciphertext = bytes(b ^ 0x42 for b in str(cookie_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
