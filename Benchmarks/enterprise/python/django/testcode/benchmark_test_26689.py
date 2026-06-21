# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26689(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
