# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest27097(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
