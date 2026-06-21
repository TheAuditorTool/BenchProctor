# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79349(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
