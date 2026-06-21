# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest69242(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
