# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01593(request):
    multipart_value = request.POST.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
