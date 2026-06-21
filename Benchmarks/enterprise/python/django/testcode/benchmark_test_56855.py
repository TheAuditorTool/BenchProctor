# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56855(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
