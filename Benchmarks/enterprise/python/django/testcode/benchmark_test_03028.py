# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import ast


def BenchmarkTest03028(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(mark_safe(\'<img src="\' + str(data) + \'">\'))', '<sink>', 'exec'))
    return _ev['r']
