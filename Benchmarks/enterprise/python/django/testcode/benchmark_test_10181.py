# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10181(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
