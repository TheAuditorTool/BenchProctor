# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25774(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
