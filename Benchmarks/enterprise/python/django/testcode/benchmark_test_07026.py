# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07026(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
