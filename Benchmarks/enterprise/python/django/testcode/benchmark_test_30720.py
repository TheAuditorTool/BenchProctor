# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30720(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
