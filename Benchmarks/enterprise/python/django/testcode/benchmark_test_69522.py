# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest69522(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    os.environ['APP_USER_PREFERENCE'] = str(json_value)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
