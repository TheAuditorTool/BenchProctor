# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07874(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
