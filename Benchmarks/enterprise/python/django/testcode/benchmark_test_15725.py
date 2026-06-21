# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15725(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
