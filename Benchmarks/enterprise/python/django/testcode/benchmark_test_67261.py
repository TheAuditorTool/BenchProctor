# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


def BenchmarkTest67261(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
