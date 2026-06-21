# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58224(request):
    multipart_value = request.POST.get('multipart_field', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(multipart_value)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
