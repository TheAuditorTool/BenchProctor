# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest62820(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not auth_check(request.session.get('user', ''), str(header_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
