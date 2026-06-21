# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34810(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    eval(str(data))
    return JsonResponse({"saved": True})
