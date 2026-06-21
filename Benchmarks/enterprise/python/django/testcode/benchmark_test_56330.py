# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56330(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
