# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest80195(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
