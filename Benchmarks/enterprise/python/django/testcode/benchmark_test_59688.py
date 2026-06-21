# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59688(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
