# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11673(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
