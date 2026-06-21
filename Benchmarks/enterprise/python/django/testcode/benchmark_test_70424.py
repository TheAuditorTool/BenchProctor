# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70424(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
