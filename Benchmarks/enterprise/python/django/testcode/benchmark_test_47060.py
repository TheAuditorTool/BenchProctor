# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest47060(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
