# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest60408(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
