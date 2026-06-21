# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62308(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
