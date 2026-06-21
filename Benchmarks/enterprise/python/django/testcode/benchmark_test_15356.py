# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest15356(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
