# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42736(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
