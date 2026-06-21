# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73764(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
