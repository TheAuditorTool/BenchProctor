# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest47304(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    processed = data[:64]
    return HttpResponse(Template(processed).render(Context()))
