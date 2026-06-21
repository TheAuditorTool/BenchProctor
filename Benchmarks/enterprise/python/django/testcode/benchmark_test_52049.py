# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52049(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
