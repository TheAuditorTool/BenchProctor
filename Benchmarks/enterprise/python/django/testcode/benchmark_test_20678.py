# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest20678(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
