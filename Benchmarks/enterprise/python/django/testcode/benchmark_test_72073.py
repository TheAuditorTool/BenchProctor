# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72073(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
