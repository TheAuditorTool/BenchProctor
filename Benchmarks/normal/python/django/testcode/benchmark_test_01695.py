# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01695(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
