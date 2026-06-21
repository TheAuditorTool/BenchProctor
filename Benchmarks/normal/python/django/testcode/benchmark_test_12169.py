# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest12169(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_check('user', str(auth_header)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
