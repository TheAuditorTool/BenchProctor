# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest39044(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    os.remove(str(data))
    return JsonResponse({"saved": True})
