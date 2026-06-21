# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42765(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
