# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32337(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
