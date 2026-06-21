# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49811(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
