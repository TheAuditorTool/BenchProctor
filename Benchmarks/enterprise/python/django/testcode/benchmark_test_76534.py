# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76534(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
