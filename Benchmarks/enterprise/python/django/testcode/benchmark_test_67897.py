# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67897(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
