# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest63243(request, path_param):
    path_value = path_param
    if not auth_check(request.session.get('user', ''), str(path_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
