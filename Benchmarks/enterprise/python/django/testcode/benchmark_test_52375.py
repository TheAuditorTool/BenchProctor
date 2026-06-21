# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52375(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
