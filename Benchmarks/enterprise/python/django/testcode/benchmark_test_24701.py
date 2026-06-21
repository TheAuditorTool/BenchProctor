# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24701(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
