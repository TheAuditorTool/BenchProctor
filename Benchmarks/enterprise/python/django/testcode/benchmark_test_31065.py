# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31065(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
