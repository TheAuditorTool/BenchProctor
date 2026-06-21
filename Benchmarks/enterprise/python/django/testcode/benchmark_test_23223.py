# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23223(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(header_value), secure=True, httponly=True, samesite='Strict')
    return resp
