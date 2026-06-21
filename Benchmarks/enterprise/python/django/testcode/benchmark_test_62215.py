# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62215(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
