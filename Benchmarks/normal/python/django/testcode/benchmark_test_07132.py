# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07132(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
