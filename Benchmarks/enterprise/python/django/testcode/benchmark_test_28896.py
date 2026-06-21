# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28896(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
