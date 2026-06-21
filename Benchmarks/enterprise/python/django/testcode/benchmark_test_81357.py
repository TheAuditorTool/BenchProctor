# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81357(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
