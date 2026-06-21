# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22505(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
