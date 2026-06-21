# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest08315(request):
    raw_body = request.body.decode('utf-8')
    digest = str(raw_body).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
