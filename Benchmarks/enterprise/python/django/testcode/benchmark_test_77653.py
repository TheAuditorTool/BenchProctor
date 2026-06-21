# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77653(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
