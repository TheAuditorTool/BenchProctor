# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68223(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
