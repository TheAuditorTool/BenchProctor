# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64


def BenchmarkTest73683(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
