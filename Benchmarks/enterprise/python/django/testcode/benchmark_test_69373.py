# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69373(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
