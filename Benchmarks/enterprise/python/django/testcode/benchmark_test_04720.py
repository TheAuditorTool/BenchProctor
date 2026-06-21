# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04720(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
