# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01339(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return JsonResponse({"saved": True})
