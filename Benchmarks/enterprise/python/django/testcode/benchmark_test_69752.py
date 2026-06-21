# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest69752(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
