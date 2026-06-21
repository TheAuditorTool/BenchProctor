# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50181(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    eval(str(data))
    return JsonResponse({"saved": True})
