# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09694(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
