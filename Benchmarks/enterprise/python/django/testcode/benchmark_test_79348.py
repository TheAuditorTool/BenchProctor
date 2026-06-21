# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


def relay_value(value):
    return value

def BenchmarkTest79348(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
