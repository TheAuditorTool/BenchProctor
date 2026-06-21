# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16577(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(referer_value))
    return resp
