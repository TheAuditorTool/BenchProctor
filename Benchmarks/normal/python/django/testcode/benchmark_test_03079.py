# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03079(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(forwarded_ip), secure=True, httponly=True, samesite='Strict')
    return resp
