# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71947(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
