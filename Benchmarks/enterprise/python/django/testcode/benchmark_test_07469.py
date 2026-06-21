# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07469(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
