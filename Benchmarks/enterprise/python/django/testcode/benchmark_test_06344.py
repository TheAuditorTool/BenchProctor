# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest06344(request):
    xml_value = request.body.decode('utf-8')
    digest = hashlib.sha256(str(xml_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
