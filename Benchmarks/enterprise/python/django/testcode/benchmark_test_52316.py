# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52316(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
