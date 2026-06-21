# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05387(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
