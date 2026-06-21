# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest36604(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
