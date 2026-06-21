# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36003(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
