# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest39234(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
