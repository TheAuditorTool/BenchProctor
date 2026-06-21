# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest13465(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
