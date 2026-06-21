# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest44687(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
