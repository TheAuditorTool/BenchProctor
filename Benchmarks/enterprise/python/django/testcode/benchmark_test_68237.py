# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest68237(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
