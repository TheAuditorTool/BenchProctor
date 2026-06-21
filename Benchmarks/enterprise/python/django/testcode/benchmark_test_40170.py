# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40170(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
