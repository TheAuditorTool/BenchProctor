# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest70766(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
