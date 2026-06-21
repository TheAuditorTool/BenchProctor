# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest35687(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
