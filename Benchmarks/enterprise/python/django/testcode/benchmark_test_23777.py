# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest23777(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
