# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64
import os


def BenchmarkTest17812(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
