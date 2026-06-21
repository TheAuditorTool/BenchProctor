# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32285(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
