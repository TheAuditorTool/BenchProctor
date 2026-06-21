# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66368(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
