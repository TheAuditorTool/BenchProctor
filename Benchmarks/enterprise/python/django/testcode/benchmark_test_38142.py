# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest38142(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
