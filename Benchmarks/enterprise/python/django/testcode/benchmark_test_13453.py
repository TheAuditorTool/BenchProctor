# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest13453(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
