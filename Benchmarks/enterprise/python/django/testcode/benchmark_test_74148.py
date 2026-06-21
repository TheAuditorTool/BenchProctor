# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74148(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
