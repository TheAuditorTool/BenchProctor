# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57819(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
