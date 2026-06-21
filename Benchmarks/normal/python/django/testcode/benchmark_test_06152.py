# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06152(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
