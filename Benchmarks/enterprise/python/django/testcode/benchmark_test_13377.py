# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest13377(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not auth_check(request.session.get('user', ''), str(forwarded_ip)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
