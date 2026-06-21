# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21129(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
