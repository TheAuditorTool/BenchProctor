# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest42366(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(json_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = json_value
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
