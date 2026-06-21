# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15104(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
