# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52813(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
