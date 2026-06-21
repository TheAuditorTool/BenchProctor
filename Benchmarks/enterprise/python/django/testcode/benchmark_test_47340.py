# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest47340(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if auth_check('user', str(header_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
