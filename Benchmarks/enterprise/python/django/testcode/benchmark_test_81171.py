# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81171(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
