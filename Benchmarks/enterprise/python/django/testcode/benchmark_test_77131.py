# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77131(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
