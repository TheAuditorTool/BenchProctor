# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest62192(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if auth_check('user', str(forwarded_ip)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
