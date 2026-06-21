# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80580(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
