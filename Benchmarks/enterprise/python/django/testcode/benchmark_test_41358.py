# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41358(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
