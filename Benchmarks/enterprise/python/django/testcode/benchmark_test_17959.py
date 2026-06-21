# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest17959(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        granted = auth_check('resource', str(ua_value))
    except Exception:
        granted = False
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
