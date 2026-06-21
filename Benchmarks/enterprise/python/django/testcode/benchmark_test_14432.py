# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest14432(request):
    raw_body = request.body.decode('utf-8')
    data = to_text(raw_body)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
