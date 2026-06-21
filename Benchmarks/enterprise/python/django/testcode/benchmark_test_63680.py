# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63680(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(ua_value), secure=True, httponly=True, samesite='Strict')
    return resp
