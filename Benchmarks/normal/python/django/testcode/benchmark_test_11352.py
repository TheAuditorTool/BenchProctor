# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest11352(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
