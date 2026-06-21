# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81259(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
