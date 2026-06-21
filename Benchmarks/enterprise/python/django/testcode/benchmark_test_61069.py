# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61069(request):
    xml_value = request.body.decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
