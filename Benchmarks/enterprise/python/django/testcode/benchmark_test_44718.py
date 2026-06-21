# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44718(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    int(str(data))
    return JsonResponse({"saved": True})
