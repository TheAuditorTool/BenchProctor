# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest10199(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    auth_check('user', forwarded_ip)
    return JsonResponse({"saved": True})
