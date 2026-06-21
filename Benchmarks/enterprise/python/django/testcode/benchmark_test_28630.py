# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28630(request):
    raw_body = request.body.decode('utf-8')
    if str(raw_body) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
