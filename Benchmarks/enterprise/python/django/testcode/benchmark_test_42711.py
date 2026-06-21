# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42711(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
