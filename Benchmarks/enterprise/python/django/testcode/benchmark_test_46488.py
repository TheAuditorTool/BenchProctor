# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46488(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
