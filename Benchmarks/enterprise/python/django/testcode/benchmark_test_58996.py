# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58996(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
