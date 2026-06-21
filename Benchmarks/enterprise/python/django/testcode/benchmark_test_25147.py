# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25147(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
