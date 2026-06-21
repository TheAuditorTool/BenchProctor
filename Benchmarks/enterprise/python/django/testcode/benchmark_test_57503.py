# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57503(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
