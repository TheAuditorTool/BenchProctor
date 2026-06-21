# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest80022(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
