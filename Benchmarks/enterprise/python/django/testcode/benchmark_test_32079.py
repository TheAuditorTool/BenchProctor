# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32079(request):
    cookie_value = request.COOKIES.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    int(str(data))
    return JsonResponse({"saved": True})
