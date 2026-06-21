# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest16171(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
