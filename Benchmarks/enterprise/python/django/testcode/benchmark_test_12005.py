# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12005(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
