# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest49987(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
