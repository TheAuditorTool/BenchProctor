# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32035(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
