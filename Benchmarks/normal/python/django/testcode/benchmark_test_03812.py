# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest03812(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
