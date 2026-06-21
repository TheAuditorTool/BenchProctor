# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10479(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
