# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13263(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
