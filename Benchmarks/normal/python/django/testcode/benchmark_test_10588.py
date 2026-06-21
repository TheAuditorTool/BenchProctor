# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest10588(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
