# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest30399(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
