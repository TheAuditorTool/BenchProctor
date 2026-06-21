# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22702(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
