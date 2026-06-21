# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61490(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
