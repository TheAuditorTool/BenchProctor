# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24668(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
