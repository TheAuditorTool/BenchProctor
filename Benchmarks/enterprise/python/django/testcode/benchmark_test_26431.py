# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26431(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(auth_header), secure=True, httponly=True, samesite='Strict')
    return resp
