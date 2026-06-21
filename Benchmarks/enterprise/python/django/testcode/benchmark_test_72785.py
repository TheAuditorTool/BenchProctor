# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest72785(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
