# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest20492(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
