# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest55509(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
