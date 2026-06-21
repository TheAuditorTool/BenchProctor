# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest73321(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
