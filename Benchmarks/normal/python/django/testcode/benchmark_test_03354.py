# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest03354(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
