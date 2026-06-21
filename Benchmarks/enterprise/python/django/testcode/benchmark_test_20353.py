# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest20353(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    def _primary():
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
