# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00011(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
