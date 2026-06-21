# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest09528(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
