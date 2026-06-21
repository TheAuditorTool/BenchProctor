# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def relay_value(value):
    return value

def BenchmarkTest70036(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
