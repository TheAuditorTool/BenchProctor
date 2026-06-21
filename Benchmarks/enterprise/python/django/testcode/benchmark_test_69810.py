# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69810(request):
    cookie_value = request.COOKIES.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
