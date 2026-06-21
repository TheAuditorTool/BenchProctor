# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest38705(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
