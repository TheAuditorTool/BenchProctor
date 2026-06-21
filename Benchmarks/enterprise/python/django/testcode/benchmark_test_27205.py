# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27205(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
