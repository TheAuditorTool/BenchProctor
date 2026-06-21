# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62041(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
