# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35163(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
