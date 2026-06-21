# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58739(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
