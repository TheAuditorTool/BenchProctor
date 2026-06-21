# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest45858(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(mark_safe(\'<img src="\' + str(data) + \'">\'))', '<sink>', 'exec'))
    return _ev['r']
