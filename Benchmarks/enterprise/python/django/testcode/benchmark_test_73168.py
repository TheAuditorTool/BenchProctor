# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73168(request):
    host_value = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
