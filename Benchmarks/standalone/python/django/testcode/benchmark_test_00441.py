# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00441(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
