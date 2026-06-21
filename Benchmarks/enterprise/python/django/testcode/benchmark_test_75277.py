# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
import os


def BenchmarkTest75277(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
