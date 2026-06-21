# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06380(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
