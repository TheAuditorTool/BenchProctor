# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35832(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
