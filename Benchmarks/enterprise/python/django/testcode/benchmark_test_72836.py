# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72836(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
