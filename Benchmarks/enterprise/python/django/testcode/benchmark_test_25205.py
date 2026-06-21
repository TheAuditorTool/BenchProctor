# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest25205(request, path_param):
    path_value = path_param
    os.remove(str(path_value))
    return JsonResponse({"saved": True})
