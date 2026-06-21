# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def relay_value(value):
    return value

def BenchmarkTest46168(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    _ev = {}
    eval(compile("with open(os.path.join('/var/app/data', str(data)), 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
