# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01283(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
