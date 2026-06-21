# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00323(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
