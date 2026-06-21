# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35501(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
