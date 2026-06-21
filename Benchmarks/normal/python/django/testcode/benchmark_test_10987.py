# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10987(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
