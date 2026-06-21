# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest57509(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
