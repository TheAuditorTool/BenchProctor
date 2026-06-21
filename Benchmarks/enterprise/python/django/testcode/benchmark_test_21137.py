# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21137(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
