# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38021(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
