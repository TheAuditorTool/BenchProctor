# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest56112(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
