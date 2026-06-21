# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80494(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
