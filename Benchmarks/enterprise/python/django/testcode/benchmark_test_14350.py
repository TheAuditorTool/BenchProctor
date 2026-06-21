# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14350(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
