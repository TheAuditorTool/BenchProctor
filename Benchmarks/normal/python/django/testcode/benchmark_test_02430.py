# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest02430(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
