# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41500(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
