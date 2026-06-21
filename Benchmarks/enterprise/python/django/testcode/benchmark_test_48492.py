# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest48492(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
