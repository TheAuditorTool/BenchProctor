# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03359(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
