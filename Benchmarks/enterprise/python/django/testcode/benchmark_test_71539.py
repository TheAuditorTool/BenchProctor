# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71539(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
