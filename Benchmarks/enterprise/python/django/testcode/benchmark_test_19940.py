# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19940(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
