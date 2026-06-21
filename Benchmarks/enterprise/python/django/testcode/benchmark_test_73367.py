# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest73367(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
