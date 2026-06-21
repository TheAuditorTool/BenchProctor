# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69898(request):
    host_value = request.META.get('HTTP_HOST', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
