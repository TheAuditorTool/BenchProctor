# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49320(request):
    cookie_value = request.COOKIES.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
