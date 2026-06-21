# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42160(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(referer_value)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
