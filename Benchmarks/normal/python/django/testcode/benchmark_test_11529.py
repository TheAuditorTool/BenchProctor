# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest11529(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
