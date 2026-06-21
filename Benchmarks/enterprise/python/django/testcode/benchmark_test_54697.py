# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest54697(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
