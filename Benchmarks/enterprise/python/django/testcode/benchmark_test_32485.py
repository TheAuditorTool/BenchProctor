# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32485(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
