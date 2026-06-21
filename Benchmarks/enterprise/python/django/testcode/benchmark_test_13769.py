# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest13769(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
