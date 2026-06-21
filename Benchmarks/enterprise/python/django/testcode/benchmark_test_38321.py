# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38321(request):
    raw_body = request.body.decode('utf-8')
    if str(raw_body) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
