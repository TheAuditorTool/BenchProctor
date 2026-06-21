# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest67131(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
