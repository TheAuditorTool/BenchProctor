# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest54699(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
