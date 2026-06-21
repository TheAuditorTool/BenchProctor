# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest08951(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
