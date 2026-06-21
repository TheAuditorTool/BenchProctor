# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47775(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
