# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest28346(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
