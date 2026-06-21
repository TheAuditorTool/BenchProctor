# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13450(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
