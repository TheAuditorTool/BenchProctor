# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52675(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
