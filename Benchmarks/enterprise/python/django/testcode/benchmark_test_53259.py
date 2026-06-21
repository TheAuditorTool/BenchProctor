# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53259(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
