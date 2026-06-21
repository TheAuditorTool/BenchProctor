# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12208(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
