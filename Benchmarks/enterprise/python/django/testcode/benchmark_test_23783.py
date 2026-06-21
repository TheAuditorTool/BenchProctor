# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23783(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
