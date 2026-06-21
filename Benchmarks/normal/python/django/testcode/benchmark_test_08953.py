# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08953(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
