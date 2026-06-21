# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest57470(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not auth_check(str(forwarded_ip), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
