# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest12237(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
