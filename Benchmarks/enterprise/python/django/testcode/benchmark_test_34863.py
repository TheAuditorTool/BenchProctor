# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest34863(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
