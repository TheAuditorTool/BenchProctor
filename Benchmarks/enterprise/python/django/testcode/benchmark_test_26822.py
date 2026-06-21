# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26822(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
