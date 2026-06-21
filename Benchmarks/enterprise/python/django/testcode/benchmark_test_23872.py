# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def relay_value(value):
    return value

def BenchmarkTest23872(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if str(processed) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
