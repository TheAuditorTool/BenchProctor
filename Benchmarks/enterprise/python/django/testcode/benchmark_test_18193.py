# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18193(request):
    host_value = request.META.get('HTTP_HOST', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
