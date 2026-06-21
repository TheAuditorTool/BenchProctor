# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55961(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(auth_header)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
