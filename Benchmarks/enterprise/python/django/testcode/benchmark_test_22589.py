# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest22589(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
