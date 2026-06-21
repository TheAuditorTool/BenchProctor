# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64


def BenchmarkTest15996(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
