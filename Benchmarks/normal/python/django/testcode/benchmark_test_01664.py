# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01664(request):
    host_value = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
