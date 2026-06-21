# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00722(request):
    host_value = request.META.get('HTTP_HOST', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(host_value), secure=True, httponly=True, samesite='Strict')
    return resp
