# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07528(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
