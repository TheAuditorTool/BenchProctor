# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest55160(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
