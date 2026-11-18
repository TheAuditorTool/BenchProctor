# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00357(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(auth_header).strip()
        case _:
            data = str(auth_header)
    exec(str(data))
    return JsonResponse({"saved": True})
