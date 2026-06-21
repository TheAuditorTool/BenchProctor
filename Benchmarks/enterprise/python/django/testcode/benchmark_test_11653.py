# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest11653(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
