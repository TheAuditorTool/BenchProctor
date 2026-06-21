# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76239(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
