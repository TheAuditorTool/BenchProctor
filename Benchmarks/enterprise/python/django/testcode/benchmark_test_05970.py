# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05970(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
