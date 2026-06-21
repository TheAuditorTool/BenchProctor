# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08561(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
