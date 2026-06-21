# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46087(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
