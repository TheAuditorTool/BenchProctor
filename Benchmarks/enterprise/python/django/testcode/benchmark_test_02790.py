# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02790(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
