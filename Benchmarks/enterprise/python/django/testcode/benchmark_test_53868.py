# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53868(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
