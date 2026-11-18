# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00026(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
