# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest19228(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not auth_check(str(header_value), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
