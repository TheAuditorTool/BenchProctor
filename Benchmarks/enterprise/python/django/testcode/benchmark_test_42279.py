# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest42279(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not auth_check(str(ua_value), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
