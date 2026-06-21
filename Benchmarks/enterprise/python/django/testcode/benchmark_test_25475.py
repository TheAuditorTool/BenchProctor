# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25475(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
