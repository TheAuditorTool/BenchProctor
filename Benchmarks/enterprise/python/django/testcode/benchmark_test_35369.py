# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35369(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
