# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest40161(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
