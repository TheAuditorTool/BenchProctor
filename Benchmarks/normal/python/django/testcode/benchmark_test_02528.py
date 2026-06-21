# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest02528(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
