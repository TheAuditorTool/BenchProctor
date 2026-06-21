# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest39461(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
