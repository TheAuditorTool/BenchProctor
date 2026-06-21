# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest66848(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
