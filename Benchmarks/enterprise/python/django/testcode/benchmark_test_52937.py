# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52937(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
