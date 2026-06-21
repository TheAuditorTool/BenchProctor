# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56125(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
