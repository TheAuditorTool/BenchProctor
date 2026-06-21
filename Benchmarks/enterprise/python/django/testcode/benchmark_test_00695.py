# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00695(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
