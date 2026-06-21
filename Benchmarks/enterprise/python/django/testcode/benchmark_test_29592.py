# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest29592(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = normalise_input(auth_header)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
