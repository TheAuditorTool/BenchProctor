# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01425(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
