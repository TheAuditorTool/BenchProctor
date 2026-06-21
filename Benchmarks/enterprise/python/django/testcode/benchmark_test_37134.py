# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest37134(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
