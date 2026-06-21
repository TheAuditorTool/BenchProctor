# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80805(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
