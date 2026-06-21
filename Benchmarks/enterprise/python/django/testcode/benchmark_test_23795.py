# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest23795(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
