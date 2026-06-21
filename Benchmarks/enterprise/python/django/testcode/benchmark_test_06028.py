# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def relay_value(value):
    return value

def BenchmarkTest06028(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
