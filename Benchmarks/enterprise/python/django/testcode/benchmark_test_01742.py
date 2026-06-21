# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01742(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
