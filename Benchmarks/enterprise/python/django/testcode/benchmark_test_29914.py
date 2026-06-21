# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29914(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
