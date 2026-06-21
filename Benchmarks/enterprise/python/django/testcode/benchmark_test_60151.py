# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60151(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
