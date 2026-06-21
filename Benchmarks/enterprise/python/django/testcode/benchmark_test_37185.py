# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37185(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
