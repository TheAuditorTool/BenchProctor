# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04231(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
