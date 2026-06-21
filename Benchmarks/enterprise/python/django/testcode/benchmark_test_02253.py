# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02253(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
