# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63182(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
