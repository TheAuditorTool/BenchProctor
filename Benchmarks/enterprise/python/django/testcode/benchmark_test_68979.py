# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68979(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
