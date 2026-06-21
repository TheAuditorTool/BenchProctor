# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56939(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
