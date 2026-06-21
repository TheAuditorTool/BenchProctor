# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79835(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    eval(str(data))
    return JsonResponse({"saved": True})
