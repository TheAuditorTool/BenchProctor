# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21476(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
