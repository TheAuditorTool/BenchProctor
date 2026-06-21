# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


def relay_value(value):
    return value

def BenchmarkTest72838(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
