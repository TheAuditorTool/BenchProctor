# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12533(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
