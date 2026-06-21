# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54292(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
