# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13296(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
