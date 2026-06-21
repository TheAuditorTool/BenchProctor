# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29919(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
