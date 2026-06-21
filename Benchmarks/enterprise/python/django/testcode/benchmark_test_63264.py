# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63264(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
