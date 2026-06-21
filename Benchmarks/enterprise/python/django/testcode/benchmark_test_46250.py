# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest46250(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
