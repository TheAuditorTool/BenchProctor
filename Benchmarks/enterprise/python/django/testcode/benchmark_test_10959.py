# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10959(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    def _primary():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
