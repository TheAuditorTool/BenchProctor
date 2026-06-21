# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25629(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
