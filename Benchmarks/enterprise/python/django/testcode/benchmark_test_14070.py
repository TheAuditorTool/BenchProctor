# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import ast


def BenchmarkTest14070(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(mark_safe(\'<img src="\' + str(data) + \'">\'))', '<sink>', 'exec'))
    return _ev['r']
