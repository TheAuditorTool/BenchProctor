# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02854(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
