# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest45365(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    eval(compile("with open('/var/www/html/exports/report.txt', 'w') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
