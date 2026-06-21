# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest20754(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
