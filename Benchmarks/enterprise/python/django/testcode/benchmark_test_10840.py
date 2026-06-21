# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest10840(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not auth_check(request.session.get('user', ''), str(ua_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
