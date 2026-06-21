# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49763(request):
    host_value = request.META.get('HTTP_HOST', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
