# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29655(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
