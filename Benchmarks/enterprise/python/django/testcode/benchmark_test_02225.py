# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02225(request):
    cookie_value = request.COOKIES.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
