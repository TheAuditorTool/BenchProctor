# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest40639(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
