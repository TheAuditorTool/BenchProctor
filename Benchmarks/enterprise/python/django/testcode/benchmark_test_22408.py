# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22408(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
