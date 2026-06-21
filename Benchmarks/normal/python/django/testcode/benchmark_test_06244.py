# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06244(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
