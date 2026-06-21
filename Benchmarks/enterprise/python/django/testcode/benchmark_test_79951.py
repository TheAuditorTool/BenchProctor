# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79951(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(origin_value), secure=True, httponly=True, samesite='Strict')
    return resp
