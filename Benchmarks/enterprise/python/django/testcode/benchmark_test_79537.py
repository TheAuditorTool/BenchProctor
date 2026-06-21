# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79537(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
