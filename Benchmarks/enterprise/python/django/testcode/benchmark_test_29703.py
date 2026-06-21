# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29703(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
