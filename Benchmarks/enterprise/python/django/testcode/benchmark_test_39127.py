# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39127(request, path_param):
    path_value = path_param
    result = 100 / int(str(path_value))
    return JsonResponse({"saved": True})
