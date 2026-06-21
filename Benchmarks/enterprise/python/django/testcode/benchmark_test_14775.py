# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest14775(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
