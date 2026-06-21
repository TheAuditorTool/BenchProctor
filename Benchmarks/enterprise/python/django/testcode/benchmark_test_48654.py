# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest48654(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
