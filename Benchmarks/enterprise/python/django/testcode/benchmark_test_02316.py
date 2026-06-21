# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02316(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
