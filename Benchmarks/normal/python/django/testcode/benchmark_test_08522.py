# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08522(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
