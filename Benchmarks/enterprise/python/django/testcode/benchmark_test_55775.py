# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest55775(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
