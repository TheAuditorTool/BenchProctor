# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05165(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
