# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46638(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    def _primary():
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
