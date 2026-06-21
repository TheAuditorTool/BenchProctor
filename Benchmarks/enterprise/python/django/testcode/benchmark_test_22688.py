# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22688(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
