# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76729(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
