# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43686(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
