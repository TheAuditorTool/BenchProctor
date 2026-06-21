# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest16927(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
