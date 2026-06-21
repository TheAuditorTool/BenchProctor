# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest04505(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
