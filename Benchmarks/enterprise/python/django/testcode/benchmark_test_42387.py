# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest42387(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
