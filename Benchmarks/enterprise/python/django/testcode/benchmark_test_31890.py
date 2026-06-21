# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest31890(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
