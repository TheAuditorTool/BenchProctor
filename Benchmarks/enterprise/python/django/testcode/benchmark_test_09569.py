# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09569(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
