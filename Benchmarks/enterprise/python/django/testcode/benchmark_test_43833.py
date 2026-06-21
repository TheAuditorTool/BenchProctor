# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43833(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
