# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29149(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
