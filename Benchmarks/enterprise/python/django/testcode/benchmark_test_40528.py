# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest40528(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not auth_check(str(auth_header), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
