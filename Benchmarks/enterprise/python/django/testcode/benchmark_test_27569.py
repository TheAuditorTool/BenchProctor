# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest27569(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.remove(str(data))
    return JsonResponse({"saved": True})
