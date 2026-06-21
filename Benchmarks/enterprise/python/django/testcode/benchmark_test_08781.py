# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08781(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
