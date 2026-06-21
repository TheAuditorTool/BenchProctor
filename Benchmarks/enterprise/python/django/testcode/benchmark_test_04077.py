# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04077(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
