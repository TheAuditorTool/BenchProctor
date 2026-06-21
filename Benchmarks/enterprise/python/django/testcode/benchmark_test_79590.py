# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest79590(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
