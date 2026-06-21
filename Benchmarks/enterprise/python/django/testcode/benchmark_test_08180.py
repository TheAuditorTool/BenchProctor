# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08180(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
