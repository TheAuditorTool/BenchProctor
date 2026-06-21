# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80043(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
