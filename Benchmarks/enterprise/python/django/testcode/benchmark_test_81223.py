# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest81223(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
