# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest45678(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
