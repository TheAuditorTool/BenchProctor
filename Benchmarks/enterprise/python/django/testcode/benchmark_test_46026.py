# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46026(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
