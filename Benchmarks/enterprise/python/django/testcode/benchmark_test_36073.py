# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36073(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
