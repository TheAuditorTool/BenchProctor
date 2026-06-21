# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54751(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
