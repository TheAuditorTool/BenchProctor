# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00309(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
