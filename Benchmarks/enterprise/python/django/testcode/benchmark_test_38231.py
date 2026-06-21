# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest38231(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
