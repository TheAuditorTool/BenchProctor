# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest46664(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
