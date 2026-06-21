# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48042(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
