# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16129(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
