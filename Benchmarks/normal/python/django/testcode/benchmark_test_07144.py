# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07144(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
