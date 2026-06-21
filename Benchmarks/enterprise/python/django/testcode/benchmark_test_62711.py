# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62711(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
