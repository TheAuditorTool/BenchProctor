# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27663(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    int(str(data))
    return JsonResponse({"saved": True})
