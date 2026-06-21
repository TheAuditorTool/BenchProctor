# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64687(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
