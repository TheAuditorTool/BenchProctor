# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03212(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
