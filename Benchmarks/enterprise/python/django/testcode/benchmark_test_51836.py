# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51836(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(header_value)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
