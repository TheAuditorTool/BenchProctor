# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54879(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
