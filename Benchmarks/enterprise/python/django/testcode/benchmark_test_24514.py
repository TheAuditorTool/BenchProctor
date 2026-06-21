# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24514(request, path_param):
    path_value = path_param
    if str(path_value) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
